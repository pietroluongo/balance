import random
from paho.mqtt import client as mqtt_client
from typing import Callable

class MQTTClient:
    def __init__(self, topic: str, callback: Callable):
        self._broker = 'localhost'
        self._port = 1883
        self._topic = topic
        self._client_id = f'python-mqtt-{random.randint(0, 100)}'
        self.connect()
        self.subscribe(callback)
        self._client.loop_start()

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self._client = mqtt_client.Client(self._client_id)
        self._client.on_connect = on_connect
        self._client.connect(self._broker, self._port)

    def subscribe(self, callback: Callable):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self._client.subscribe(self._topic)
        self._client.on_message = callback
