#include <PushButton.h>
#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>

SoftwareSerial bt(2,3); // btTXD - 2, btRXD - 3
LiquidCrystal_I2C lcd(0x27, 20, 4); // SDA - A4, SCL - A5

#define BT_POWER 4
#define RESET_BUTTON 5
#define DATA_BUTTON 6
#define PING_TIMEOUT 2000 //in ms
#define ADD_MAJOR 7
#define SUB_MAJOR 8
#define ADD_MINOR 9
#define SUB_MINOR 10

#define ACC_CHAR "!"
#define PRES_CHAR "@"
#define PING_CHAR "#"
#define SCORE_RESET_CHAR "$"
#define END_CHAR "~"
#define RESET_CHAR "%"


int IMODE = 0;
String CNAME = "NO COMPETITOR";
bool RESET_SIG = false;
float score[2];
unsigned long last_ping;


PushButton reset_pb(RESET_BUTTON);
PushButton data_pb(DATA_BUTTON);
PushButton add_major_pb(ADD_MAJOR);
PushButton sub_major_pb(SUB_MAJOR);
PushButton add_minor_pb(ADD_MINOR);
PushButton sub_minor_pb(SUB_MINOR);

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

bool interface_available(){
  switch(IMODE){
    case 0:
      return Serial.available();
      break;
    case 1:
      return bt.available();
      break;
    default:
      break;
  }
}

char interface_read(){
  switch(IMODE){
    case 0:
      return Serial.read();
      break;
    case 1:
      return bt.read();
      break;
    default:
      break;
  }
}

String interface_readuntil(char c){
  switch(IMODE){
    case 0:
      return Serial.readStringUntil(c);
      break;
    case 1:
      return bt.readStringUntil(c);
      break;
    default:
      break;
  }
}

bool reset_char_received(){
  if(interface_available()){
    char c = interface_read();
    if(c == '%'){
      String t_str = interface_readuntil('~');
      if(t_str.length() < 20){
        CNAME = t_str;
      } else{
        CNAME = t_str.substring(0,20);
      }
      RESET_SIG = true;
      return true;
    }
  }
  return false;
}

void send_ping(){
  if(millis() - last_ping >= PING_TIMEOUT){
    interface_write(PING_CHAR);
    last_ping = millis();
  }
}

void reset_bt(){
  Serial.println("Hit reset");
  digitalWrite(BT_POWER, LOW);
  delay(1000);
  digitalWrite(BT_POWER, HIGH);  
}

void update_all_pb(){
  reset_pb.update();
  data_pb.update();
  add_major_pb.update();
  sub_major_pb.update();
  add_minor_pb.update();
  sub_minor_pb.update();
}

void acc_lcd_update(float acc){
  char res[5];
  lcd.setCursor(8,2);
  dtostrf(acc, 1, 1, res);
  lcd.print(res);
}

void acc_mode(){
  float acc = 4.0;
  lcd.setCursor(floor((20-CNAME.length())/2),0);
  lcd.print(CNAME);
  lcd.setCursor(0,2);
  lcd.print("ACC:");
  while(true){
    update_all_pb();
    acc_lcd_update(acc);
    send_ping();
    
    if(reset_char_received()) break;
    
    if(reset_pb.isClicked()){
      reset_bt();
    }
    if(data_pb.isHeld()){
      score[0] = acc;
      lcd.clear();
      break;
    }

    if(add_major_pb.isClicked()){
      if(acc + 0.3 >= 4.0)  acc = 4.0;
      else  acc += 0.3;
    }
    if(sub_major_pb.isClicked()){
      if(acc - 0.3 <= 0.0)  acc = 0.0;
      else  acc -= 0.3;
    }
    if(add_minor_pb.isClicked()){
      if(acc + 0.1 >= 4.0)  acc = 4.0;
      else  acc += 0.1;
    }
    if(sub_minor_pb.isClicked()){
      if(acc - 0.1 <= 0.0)  acc = 0.0;
      else  acc -= 0.1;
    }
  }
}

void pres_lcd_update(int mode, float p[]){
  char res[5];
  lcd.setCursor(0,1);
  switch(mode){
    case 0:
      lcd.print("SPEED & POWER       ");
      lcd.setCursor(0,2);

      dtostrf(p[0], 1, 1, res);
      lcd.print(res);
      break;
    case 1:
      lcd.print("STR, SPD, RHYTHM    ");
      lcd.setCursor(0,2);

      dtostrf(p[1], 1, 1, res);
      lcd.print(res);
      break;
    case 2:
      lcd.print("EXPRESSION OF ENERGY");
      lcd.setCursor(0,2);

      dtostrf(p[2], 1, 1, res);
      lcd.print(res);
      break;
    default:
      break;
  }
  float tot = 0;
  for(int i = 0; i < 3; i++){
    tot += p[i];
  }
  dtostrf(tot, 2, 1, res);

  lcd.setCursor(0,3);
  lcd.print("Total:");
  lcd.print(res);
}

void pres_mode(){
  float pres[3] = {2.0, 2.0, 2.0};
  int section = 0;
  lcd.setCursor(floor((20-CNAME.length())/2),0);
  lcd.print(CNAME);
  
  while(true){
    update_all_pb();   
    pres_lcd_update(section, pres);
    send_ping();
    if(reset_char_received()) break;

    
    if(reset_pb.isClicked()){
      reset_bt();
    }
    
    if(data_pb.isHeld()){
      float tot = 0;
      for(int i = 0; i < 3; i++){
        tot += pres[i];
      }
      score[1] = tot;
      lcd.clear();
      break;
    }

    if(add_major_pb.isClicked()){
      if(section + 1 >= 3)  section = 0;
      else  section += 1;
    }
    if(sub_major_pb.isClicked()){
      if(section - 1 < 0)  section = 2;
      else  section -= 1;   
    }
    if(add_minor_pb.isClicked()){
      if(pres[section] + 0.1 >= 2.0)  pres[section] = 2.0;
      else  pres[section] += 0.1;
    }
    if(sub_minor_pb.isClicked()){
      if(pres[section] - 0.1 <= 0.0)  pres[section] = 0.0;
      else  pres[section] -= 0.1;
    }
  }
}

void total_lcd_update(){
  char res[5];
  lcd.setCursor(1,0);
  lcd.print("WAIT FOR NEXT SYNC");
  lcd.setCursor(0,1);
  dtostrf(score[0], 2, 1, res);
  lcd.print("Acc: ");
  lcd.print(res);
  lcd.setCursor(0,2);
  
  dtostrf(score[1], 2, 1, res);
  lcd.print("Pres: ");
  lcd.print(res);
  lcd.setCursor(0,3);

  dtostrf(score[0] + score[1], 2, 1, res);
  lcd.print("Total: ");
  lcd.print(res);
}

void total_mode(){
  while(true){
    update_all_pb();   
    total_lcd_update();
    send_ping();
    if(reset_char_received()) break;

    
    if(reset_pb.isClicked()){
      reset_bt();
    }
    
    if(data_pb.isHeld()){
    }

    if(add_major_pb.isClicked()){
    }
    if(sub_major_pb.isClicked()){
    }
    if(add_minor_pb.isClicked()){
    }
    if(sub_minor_pb.isClicked()){
    }
  } 
}

void send_acc(){
  char res[5];
  dtostrf(score[0], 1, 1, res);
  interface_write(ACC_CHAR);
  interface_write(res);
  interface_write(END_CHAR);
}

void send_pres(){
  char res[5];
  dtostrf(score[1], 1, 1, res);
  interface_write(PRES_CHAR);
  interface_write(res);
  interface_write(END_CHAR);
}

void send_score_reset(){
  interface_write(SCORE_RESET_CHAR);
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


  add_major_pb.disableDoubleClick();
  sub_major_pb.disableDoubleClick();
  add_minor_pb.disableDoubleClick();
  sub_minor_pb.disableDoubleClick();
  
  score[0] = 0.0;
  score[1] = 0.0;
 
}

void loop() {
  // put your main code here, to run repeatedly:
  RESET_SIG = false;
  acc_mode();
  if(RESET_SIG) goto reset_sig;
  send_acc();
  
  pres_mode();
  if(RESET_SIG) goto reset_sig;
  send_pres();
  
  total_mode();

  reset_sig:
  lcd.clear();
  lcd.setCursor(6,1);
  lcd.print("SYNCING");
  lcd.setCursor(8,2);
  lcd.print("NEXT");
  delay(3000);
  lcd.clear();
  send_score_reset();
}
