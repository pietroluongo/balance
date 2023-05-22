#include <Arduino.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>
#include <Servo.h>
#include <wifiStuff.h>

// #include <ESP8266WiFi.h>
#include <WiFi.h>
#include <string>

const bool SHOULD_PRINT = false;

Servo servo;
Servo servo2;

#define SERVO_PIN 14   // GPIO13
#define SERVO_2_PIN 26 // GPIO14

WiFiClient espClient;
PubSubClient client(espClient);

StaticJsonDocument<1024> doc;

int m1 = 0;
int m2 = 0;

void callback(char *topic, byte *message, unsigned int length) {
  if (SHOULD_PRINT) {
    Serial.println("Callback");
    Serial.print("Message arrived on topic: ");
    Serial.print(topic);
    Serial.print(". Message: ");
  }
  char json[1024];
  for (unsigned int i = 0; i < length; i++) {
    if (SHOULD_PRINT) {
      Serial.print((char)message[i]);
    }
    json[i] = (char)message[i];
  }
  // Serial.println();
  DeserializationError error = deserializeJson(doc, json);
  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return;
  }
  // global_pos = doc["pos"];
  // Serial.printf("%d\n", global_pos);
  m1 = doc["m1"];
  m2 = doc["m2"];
  // Serial.printf("Got following coordinates: %d\n", global_pos);
  // Serial.printf("Got following data: (m1, m2) = (%d, %d)\n", m1, m2);
}

void setup() {
  Serial.begin(115200);

  pinMode(SERVO_PIN, OUTPUT);
  pinMode(SERVO_2_PIN, OUTPUT);

  servo.attach(SERVO_PIN);
  servo.write(0);

  servo2.attach(SERVO_2_PIN);
  servo2.write(0);
  setup_wifi(client);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect(client);
  }
  client.loop();
  servo.write(m1);
  servo2.write(m2);
  // for (int pos = 0; pos <= 180;
  //      pos += 1) { // goes from 0 degrees to 180 degrees
  //   // in steps of 1 degree
  //   servo.write(pos);        // tell servo to go to position in variable
  //   'pos' servo2.write(180 - pos); // tell servo to go to position in
  //   variable 'pos' delay(15);               // waits 15ms for the servo to
  //   reach the position
  // }
  // for (int pos = 180; pos >= 0;
  //      pos -= 1) {           // goes from 180 degrees to 0 degrees
  //   servo.write(pos);        // tell servo to go to position in variable
  //   'pos' servo2.write(180 - pos); // tell servo to go to position in
  //   variable 'pos' delay(15);               // waits 15ms for the servo to
  //   reach the position
  // }
  // for (int i = 0; i < 3; i++) {
  //   delay(200);
  //   Serial.printf("writing %d\n", i * 90);
  //   servo.write(90 * i);
  //   servo2.write(90 * i);
  // }
  // servo.write(45);
  // delay(500);
  // servo.write(135);
  // delay(500);
}