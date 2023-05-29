#include <Arduino.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>
#include <Servo.h>
#include <wifiStuff.h>

#include <WiFi.h>
#include <cstring>
#include <string>

Servo servo;
Servo servo2;

#define SERVO_PIN 14   // GPIO13
#define SERVO_2_PIN 26 // GPIO14

WiFiClient espClient;
PubSubClient client(espClient);

StaticJsonDocument<1024> doc;

int posX, posY = 0;

struct PID {
  float kp;
  float ki;
  float kd;
};

PID pid_m0 = {0};
PID pid_m1 = {0};

const int targetX = 329;
const int targetY = 227;

void updatePIDStuff();

void callback(char *topic, byte *message, unsigned int length) {
  char json[1024];
  for (unsigned int i = 0; i < length; i++) {
    json[i] = (char)message[i];
  }
  DeserializationError error = deserializeJson(doc, json);
  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return;
  }
  if (strcmp(topic, "/balance/m0/pid") == 0) {
    pid_m0.kp = doc["p"];
    pid_m0.ki = doc["i"];
    pid_m0.kd = doc["d"];
    Serial.printf("Got following M0 PID values: (%f, %f, %f)\n", pid_m0.kp,
                  pid_m0.ki, pid_m0.kd);
  } else if (strcmp(topic, "/balance/m1/pid") == 0) {
    pid_m1.kp = doc["p"];
    pid_m1.ki = doc["i"];
    pid_m1.kd = doc["d"];
    Serial.printf("Got following M1 PID values: (%f, %f, %f)\n", pid_m1.kp,
                  pid_m1.ki, pid_m1.kd);
  }

  if (strcmp(topic, "/balance/ball") == 0) {
    posX = doc["x"];
    posY = doc["y"];
    updatePIDStuff();
  }
}

int lastDeltaY = 0;
int lastDeltaX = 0;

void updatePIDStuff() {
  int p = targetY - posY;
  int d = p - lastDeltaY;
  lastDeltaY = p;
  int output = -(p * pid_m0.kp + d * pid_m0.kd) / 0.44;
  servo.write(90 + output);

  p = targetX - posX;
  d = p - lastDeltaX;
  lastDeltaX = p;
  output = -(p * pid_m1.kp + d * pid_m1.kd) / 0.44;
  Serial.printf("Output: %d\n", output);
  servo2.write(90 + output);
}

void setup() {
  Serial.begin(115200);

  pinMode(SERVO_PIN, OUTPUT);
  pinMode(SERVO_2_PIN, OUTPUT);

  servo.attach(SERVO_2_PIN);
  servo.write(90);

  servo2.attach(SERVO_PIN);
  servo2.write(90);

  setup_wifi(client);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect(client);
  }
  client.loop();
}