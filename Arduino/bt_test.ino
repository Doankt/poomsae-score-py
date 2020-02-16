#include <PushButton.h>
#include <SoftwareSerial.h>

int i = 0;
SoftwareSerial bt(2,3);
int RESET_BUTTON = 5;
int BT_POWER = 4;
int DATA_BUTTON = 6;

float score[2];

PushButton reset_pb(RESET_BUTTON);
PushButton data_pb(DATA_BUTTON);


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
    
    Serial.println("Added data");
    bt.write("<");

    dtostrf(score[0], 2, 1, res);
    bt.write(res);
    
    bt.write(",");

    dtostrf(score[1], 2, 3, res);
    bt.write(res);
    bt.write(">");
  }
}
