#include <PushButton.h>
#include <SoftwareSerial.h>

SoftwareSerial bt(2,3);
int RESET_BUTTON = 5;
int BT_POWER = 4;
int DATA_BUTTON = 6;
int PING_TIMEOUT = 2000; //in ms

int imode = 0;

float score[2];
unsigned long last_ping;


PushButton reset_pb(RESET_BUTTON);
PushButton data_pb(DATA_BUTTON);

void interface_write(const char* str){
  switch(imode){
    case 0:
      Serial.write(str);
      break;
    case 1:
      bt.write(str);
    default:
      break;
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  bt.begin(9600);


  pinMode(RESET_BUTTON, INPUT);
  
  pinMode(BT_POWER, OUTPUT);
  digitalWrite(BT_POWER, HIGH);

  pinMode(DATA_BUTTON, INPUT);

  score[0] = 2.4;
  score[1] = 4.2;
 
}

void loop() {
  // put your main code here, to run repeatedly:
  reset_pb.update();
  data_pb.update();

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

    dtostrf(score[1], 2, 3, res);
    interface_write(res);
    interface_write(">");
  }

  
  if(millis() - last_ping >= PING_TIMEOUT){
    interface_write("#");
    last_ping = millis();
  }
}
