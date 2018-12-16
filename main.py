import os
import numpy as np
from PIL import Image
import cv2
import sqlite3
import serial
import serial.tools.list_ports

ser = serial.Serial()
ports = list(serial.tools.list_ports.comports())
conn = sqlite3.connect("DetectedFaces.db")
c = conn.cursor()
c.execute ( "CREATE TABLE IF NOT EXISTS kayitli_kisiler(id int, isim text, soyad text)" )

def arduinoyu_bagla(secim):
    if secim == "1":
        ser.port =  '/dev/ttyUSB0'   # open serial port
        ser.open()
        print("'ttyUSB0' portundan bağlantı sağlandı.")

    elif secim == "2":
        ser.port = "com1"
        ser.open()
        print("'com1' portundan bağlantı sağlandı.")
    else:
        print(secim)
    return secim


def kaydet(isim, soyad):
    faceDetect = cv2.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
    cam = cv2.VideoCapture ( 0 )

    c.execute ( 'select id from kayitli_kisiler' )
    kayitli_kisi_sayisi = len ( c.fetchall () )

    id_ = kayitli_kisi_sayisi + 1
    cmd = "SELECT * FROM kayitli_kisiler WHERE id=" + str ( id_ )
    cursor = c.execute ( cmd )

    c.execute ( 'insert into kayitli_kisiler values(?,?,?)', (id_, isim, soyad) )
    conn.commit ()

    if len ( c.execute ( "select id from kayitli_kisiler where id={}".format ( int ( id_ ) ) ).fetchall () ) > 1:
        print ( "Aynı id numarası daha önce kullanılmış. Lütfen yeni bir id no ile tekrar deneyiniz." )
        c.execute (
            "delete from kayitli_kisiler where rowid not in (select min(rowid) from kayitli_kisiler group by id)" )

    else:
        sampleNum = 0
        while (True):
            ret, img = cam.read ()
            gray = cv2.cvtColor ( img, cv2.COLOR_BGR2GRAY )
            faces = faceDetect.detectMultiScale ( gray, 1.3, 5 )
            for (x, y, w, h) in faces:
                sampleNum = sampleNum + 1
                cv2.imwrite ( 'dataSet/Kullanici.' + str ( id_ ) + '.' + str ( sampleNum ) + '.jpg',
                              gray [y:y + h, x:x + w] )
                cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 0, 225), 2 )
                cv2.waitKey ( 100 )
            cv2.imshow ( 'Yuz', img )
            cv2.waitKey ( 1 )
            if (sampleNum > 5):
                break
        cam.release ()
        cv2.destroyAllWindows ()
        conn.commit ()
        print ( "kayıt başarılı olmuştur." )



def id_bul(id_):
    id_no = str ( kaydet.__get__ ( id_, int ) )
    id_no_split = id_no.split ( ">" ) [0]
    id_no_split1 = id_no.split ( (">") ) [0].split ( "of " ) [1]
    Kayit_Ekrani.retranslateUi(id_no_split1)



def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create ()
    path = 'dataSet'

    def getImagesWithID (path):
        imagePaths = [os.path.join ( path, f ) for f in os.listdir ( path )]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open ( imagePath ).convert ( 'L' )
            faceNp = np.array ( faceImg, 'uint8' )
            ID = int ( os.path.split ( imagePath ) [-1].split ( '.' ) [1] )
            faces.append ( faceNp )
            IDs.append ( ID )
            cv2.imshow ( 'egitim', faceNp )
            cv2.waitKey ( 10 )
        return np.array ( IDs ), faces

    IDs, faces = getImagesWithID ( path )
    recognizer.train ( faces, IDs )
    recognizer.save ( 'trainner/egitimData.yml' )
    cv2.destroyAllWindows ()


def getprofile(id_):
    cmd = "SELECT isim from kayitli_kisiler WHERE id=" + str(id_)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row

    cmd = "select soyad from kayitli_kisiler where id=" + str(id_)
    cursor = conn.execute(cmd)
    profile1 = None
    for row in cursor:
        profile1 = row
    return profile, profile1


def detect():
    faceDetect = cv2.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
    cam = cv2.VideoCapture ( 0 )
    rec = cv2.face.LBPHFaceRecognizer_create ()
    rec.read ( 'trainner/egitimData.yml' )
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:

            id_, conf = rec.predict(gray [y:y + h, x:x + w])
            profile = getprofile(id_)[0]
            profile1 = getprofile ( id_ ) [1]
            print(conf)
            if conf < 50:
                if profile is not None:
                    if ser.isOpen () == True:
                        ser.write ( b'1' )  # write a string
                    cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 255, 0), 2 )
                    print ( profile )
                    cv2.putText ( img, ("Isim: " + profile [0]), (x, y + h + 30), font, 0.8, (0, 255, 0), 2 )
                    cv2.putText ( img, ("Soyisim: " + profile1 [0]), (x, y + h + 60), font, 0.8, (0, 255, 0), 2 )
            elif conf > 50:
                cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 0, 225), 2 )
                print("Sisteme Kayıtlı değil!")
                cv2.putText ( img, "Sisteme Kayitli Degil!", (x, y + h + 30), font, 0.6, (255, 122, 122), 2 )
                if ser.isOpen () == True:
                    ser.write ( b'2' )  # write a string

        cv2.imshow ( 'Yuz Tanimlama', img )
        if cv2.waitKey ( 10 ) == ord ( 'q' ):
            break
    cam.release ()
    cv2.destroyAllWindows ()
