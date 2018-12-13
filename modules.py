import os
import numpy as np
from PIL import Image
import cv2
import sqlite3
import serial
import serial.tools.list_ports

ser = serial.Serial()
ports = list(serial.tools.list_ports.comports())
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



conn = sqlite3.connect("DetectedFaces.db")
c = conn.cursor()


def kaydet(id, isim, cins):
    conn = sqlite3.connect ( "DetectedFaces.db" )
    faceDetect = cv2.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
    cam = cv2.VideoCapture ( 0 )


    c = conn.cursor ()
    c.execute ( "CREATE TABLE IF NOT EXISTS isimler(id int, isim text, cinsiyet text)" )



    cmd = "SELECT * FROM isimler WHERE id=" + str ( id )
    cursor = conn.execute ( cmd )
    recordExists = 0
    for row in cursor:
        print(row)
        recordExists = 1
    if (recordExists == 1):
        cmd = "UPDATE isimler SET isim=' " + str ( isim ) + " ' WHERE id=" + str ( id )
        conn.execute(cmd)
        cmd = "UPDATE isimler SET cinsiyet=' " + str ( cins ) + " ' WHERE id=" + str ( id )
        conn.execute(cmd)
    else:
        cmd = "INSERT INTO isimler(id,isim) Values(" + str ( id ) + ",' " + str ( isim ) + " ' )"
        conn.execute ( cmd )
    conn.commit ()
    conn.close ()

    sampleNum = 0
    while (True):
        ret, img = cam.read ()
        gray = cv2.cvtColor ( img, cv2.COLOR_BGR2GRAY )
        faces = faceDetect.detectMultiScale ( gray, 1.3, 5 )
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1
            cv2.imwrite ( 'dataSet/Kullanici.' + str ( id ) + '.' + str ( sampleNum ) + '.jpg', gray [y:y + h, x:x + w] )
            cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 0, 225), 2 )
            cv2.waitKey ( 100 )
        cv2.imshow ( 'Yuz', img )
        cv2.waitKey ( 1 )
        if (sampleNum > 20):
            break
    cam.release ()
    cv2.destroyAllWindows ()


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


def getprofile(id):
    cmd = "SELECT isim from isimler WHERE id=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    return profile


def detect():
    faceDetect = cv2.CascadeClassifier ( 'haarcascade_frontalface_default.xml' )
    cam = cv2.VideoCapture ( 0 )
    rec = cv2.face.LBPHFaceRecognizer_create ()
    rec.read ( 'trainner/egitimData.yml' )
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img = cam.read ()
        gray = cv2.cvtColor ( img, cv2.COLOR_BGR2GRAY )
        faces = faceDetect.detectMultiScale ( gray, 1.3, 5 )
        for (x, y, w, h) in faces:

            id, conf = rec.predict ( gray [y:y + h, x:x + w] )
            profile = getprofile ( id )

            if conf < 50:
                if profile is not None:
                    if ser.isOpen() == True:
                        ser.write ( b'1' )  # write a string
                    cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 255, 0), 2 )
                    print ( profile )
                    cv2.putText ( img, ("isim: " + profile [0]), (x, y + h + 30), font, 0.8, (0, 255, 0), 2 )
            elif conf > 50:
                cv2.rectangle ( img, (x, y), (x + w, y + h), (0, 0, 225), 2 )
                print("Sisteme Kayıtlı değil!")
                cv2.putText ( img, "Sisteme Kayitli Degil!", (x, y + h + 30), font, 0.6, (255, 0, 0), 2 )
                if ser.isOpen() == True:
                    ser.write ( b'2' )  # write a string
        cv2.imshow ( 'Yuz', img )
        if cv2.waitKey ( 10 ) == ord ( 'q' ):
            break
    cam.release ()
    cv2.destroyAllWindows ()

