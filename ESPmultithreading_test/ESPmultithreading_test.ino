TaskHandle_t Task1;
// 1000 ticks per rev
String direction1 = "";  // handles up and down
int speed1 = 0;
int count1 = 0;
String direction2 = "";  //handles left and right
int speed2 = 0;
int count2 = 0;
int speed = 0;
String msg = "";
int UniSpeed = 1000;
int x;
int delay1 = 0;
int delay2 = 0;
int delaymiddleman1 =0; 
int delaymiddleman2 =0;
void setup(){
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(14,OUTPUT);
  pinMode(27,OUTPUT);
  

  Serial.begin(9600);
  delay(1000);
  Serial.println("ESP32 Test");
  xTaskCreatePinnedToCore(
      motorLoop, /* Function to implement the task */
      "motorLoop", /* Name of the task */
      10000,  /* Stack size in words */
      NULL,  /* Task input parameter */
      0,  /* Priority of the task */
      &Task1,  /* Task handle. */
      0); /* Core where the task should run */
}

void motorLoop(void * parameter){
  for(;;){
    // delay1=1000;
    // delay2=1000;
    // delay(1000);
    if (delay1 != delaymiddleman1 || delay2 != delaymiddleman2 ){
      delaymiddleman1 = delay1;
      delaymiddleman2 = delay2;
      // Serial.println("updated delays")
    }
    if (direction1 != "" && direction1 != "N" && delay1 != 0) {
      digitalWrite(13, HIGH);     // Output high
      delayMicroseconds(delaymiddleman1);  // set rotate speed
      digitalWrite(13, LOW);      // Output low
      delayMicroseconds(delaymiddleman1);  // set rotate speed
    }
    if (direction2 != "" && direction2 != "N" && delay2 != 0) {
      digitalWrite(14, HIGH);      // Output high
      delayMicroseconds(delaymiddleman2);  // set rotate speed
      digitalWrite(14, LOW);       // Output low
      delayMicroseconds(delaymiddleman2);  // set rotate speed
    }
  //  Serial.print("Motor running on core ");
      // Serial.println(xPortGetCoreID());
  }
}
void loop(){

  // // Serial.println("Hello");  
  // // delay(1000);
  if (Serial.available()>4) {
  //   test = Serial.read();
  //   Serial.println("test");

    msg = (Serial.readStringUntil('\n'));  // format is (letter)(2digit zero index percentage)(letter)(2digit zero index percentage)
    if (msg == "ESTOP") {
      direction1 = "";  // handles up and down
      speed1 = 0;
      direction2 = "";  //handles left and right
      speed2 = 0;
      speed = 0;
    } else {
      direction1 = msg.substring(0, 1);
      speed1 = msg.substring(1, 3).toInt();  //tenths of a degree per second
      delay1 = speed1 * 25;
      direction2 = msg.substring(3, 4);
      speed2 = msg.substring(4, 6).toInt();  //tenths of a degree per second
      delay2 = speed2 * 25;
      if (direction1 == "d") {
        digitalWrite(27, LOW);
      } else if (direction1 == "u") {
        digitalWrite(27, HIGH);
      } else {
        direction1 = "";
        delay1 = 0;
      }
      if (direction2 == "r") {
        digitalWrite(12, LOW);
      } else if (direction2 == "l") {
        digitalWrite(12, HIGH);
      } else {
        direction2 = "";
        delay2 = 0;
      }
      Serial.print("direction1 "); Serial.println(direction1);
      Serial.print("delay1 "); Serial.println(delay1);
      Serial.print("direction2 "); Serial.println(direction2);
      Serial.print("delay2 "); Serial.println(delay2);
      delay(2);
      // Serial.println(xPortGetCoreID());
    }
  }
}
