#include <SoftwareSerial.h>

SoftwareSerial bt_iletisim(7,6);

void blink(int LEDPin){
  //kendimize ait bir fonksiyon yazıyoruz
  Serial.print(LEDPin-1);
  Serial.println(". led yanmaktadir.");
  
  digitalWrite(LEDPin, HIGH);   // Ledi yakıyoruz
  delay(50);                  // bir saniye led açık durumda bekliyoruz
  digitalWrite(LEDPin, LOW);    // ledi kapıyoruz
  delay(10);
  
}
void setup(){
  for(int i=2; i<4; i++){ pinMode(i, OUTPUT);}  // 2-11 arası pinleri ayarlıyoruz
  Serial.begin(9600);
  bt_iletisim.begin(9600);
}

void loop(){
  if (Serial.available() or bt_iletisim.available()) {

    //serialden karakter alıyoruz
    char ser = Serial.read();
    char data = bt_iletisim.read();
    
    //Serial'den okunan değer "char" yani karakter formatındadır. Yani "int" değer değildir.
    //Bu nedenle case ifadelerinde tırnak içinde koşul koyuyoruz
  
if (data == '1' or ser == '1')
{

  blink(2);
}

else if (data == '2' or ser == '2')
{
blink(3);
}


}
}
