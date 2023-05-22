import random
from paho.mqtt import client as mqtt_client

BROKER = 'localhost'
PORT = 1883
TOPC = "python/mqtt"

client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt(_on_connect, _on_disconnect):
    print("Connecting to MQTT Broker...")
    def on_connect(_, __, ___, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    # client.on_disconnect = on_disconnect
    client.connect(BROKER, PORT)
    return client
