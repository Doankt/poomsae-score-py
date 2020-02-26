#include <PushButton.h>
#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>

SoftwareSerial bt(2,3); // btTXD - 2, btRXD - 3
LiquidCrystal_I2C lcd(0x27, 20, 4); // SDA - A4, SCL - A5

#define BT_POWER 4
#define RESET_BUTTON 5
#define DATA_BUTTON 6
#define PING_TIMEOUT 2000 //in ms

int IMODE = 0;

float score[2];
unsigned long last_ping;


PushButton reset_pb(RESET_BUTTON);
PushButton data_pb(DATA_BUTTON);
//PushButton add_major_pb();
//PushButton add_minor_pb();
//PushButton sub_major_pb();
//PushButton sub_minor_pb();

void interface_write(const char* str){
  switch(IMODE){
    case 0:
      Serial.write(str);
      break;
    case 1:
      bt.write(str);
      break;
    default:
      break;
  }
}

void update_lcd(){
	lcd.setCursor(0,0);
  char res[5];
  dtostrf(score[0], 2, 1, res);
	lcd.print("Acc: ");
	lcd.print(res);
	lcd.setCursor(0,1);
	
	dtostrf(score[1], 2, 1, res);
	lcd.print("Pres: ");
	lcd.print(res);
	lcd.setCursor(0,2);

	dtostrf(score[0] + score[1], 2, 1, res);
	lcd.print("Total: ");
  lcd.print(res);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  bt.begin(9600);
  
  lcd.init();
  lcd.backlight();

  pinMode(RESET_BUTTON, INPUT);
  
  pinMode(BT_POWER, OUTPUT);
  digitalWrite(BT_POWER, HIGH);

  pinMode(DATA_BUTTON, INPUT);

  score[0] = 0.0;
  score[1] = 0.0;
 
}

void loop() {
  // put your main code here, to run repeatedly:
  reset_pb.update();
  data_pb.update();
  update_lcd();



  if(reset_pb.isClicked()){
    Serial.println("Hit reset");
    digitalWrite(BT_POWER, LOW);
    delay(1000);
    digitalWrite(BT_POWER, HIGH);
  }
  
  if(data_pb.isClicked()){
    char res[5];

    score[0] = random(4*100) / 100.0;
    score[1] = random(6.0*100) / 100.0;
    
    interface_write("<");

    dtostrf(score[0], 2, 1, res);
    interface_write(res);
    
    interface_write(",");

    dtostrf(score[1], 2, 1, res);
    interface_write(res);
    interface_write(">");
    Serial.print("AA\n");
  }

  
  if(millis() - last_ping >= PING_TIMEOUT){
    interface_write("#");
    last_ping = millis();
  }
}
