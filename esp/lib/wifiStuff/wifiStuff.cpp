#include "./wifiStuff.h"
#include "./secret.h"
#include <Arduino.h>
// #include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WiFi.h>

void reconnect(PubSubClient &client) {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
      // Subscribe
      // client.subscribe("/balance/debug/setPosition");
      // client.subscribe("/balance/debug/m0");
      // client.subscribe("/balance/debug/m1");
      client.subscribe("/balance/ball");
      client.subscribe("/balance/m0/pid");
      client.subscribe("/balance/m1/pid");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup_wifi(PubSubClient &client) {
  delay(10);
  // We start by connecting t o a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WIFI_SSID);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  client.setServer(BROKER_IP, BROKER_PORT);
}
