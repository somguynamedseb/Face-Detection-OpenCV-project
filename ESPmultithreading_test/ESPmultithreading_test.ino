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
float delay1 = 0.0;
float delay2 = 0.0;
void setup(){
  
  Serial.begin(115200);
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
    delay(1000);
    if (direction1 != "" && direction1 != "N" && delay1 > 0.5) {
      digitalWrite(11, HIGH);     // Output high
      delayMicroseconds(delay1);  // set rotate speed
      digitalWrite(11, LOW);      // Output low
      delayMicroseconds(delay1);  // set rotate speed
    }
    if (direction2 != "" && direction2 != "N" && delay2 > 0.5) {
      digitalWrite(9, HIGH);      // Output high
      delayMicroseconds(delay2);  // set rotate speed
      digitalWrite(9, LOW);       // Output low
      delayMicroseconds(delay2);  // set rotate speed
    }
   Serial.print("Motor running on core ");
      Serial.println(xPortGetCoreID());
  }
}
void loop(){

  // // Serial.println("Hello");  
  // // delay(1000);
  if (Serial.available()>1) {
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
      direction2 = msg.substring(3, 4);
      speed2 = msg.substring(4, 6).toInt();  //tenths of a degree per second
      if (direction1 == "d") {
        digitalWrite(10, LOW);
      } else if (direction1 == "u") {
        digitalWrite(10, HIGH);
      } else {
        direction1 = "";
        speed1 = 0;
      }
      if (direction2 == "r") {
        digitalWrite(8, LOW);
      } else if (direction2 == "l") {
        digitalWrite(8, HIGH);
      } else {
        direction2 = "";
        speed2 = 0;
      }
      Serial.print("direction1 "); Serial.println(direction1);
      Serial.print("speed1 "); Serial.println(speed1);
      Serial.print("direction2 "); Serial.println(direction2);
      Serial.print("speed2 "); Serial.println(speed2);
      Serial.print("^^^ running on core ");
      Serial.println(xPortGetCoreID());
    }
  }
}
