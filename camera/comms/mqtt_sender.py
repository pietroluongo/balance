import random
from paho.mqtt import client as mqtt_client

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Sender(object, metaclass=Singleton):
    def __init__(self):
        self._broker = "localhost"
        self._port = 1883
        self._topic = "python/mqtt"
        self._client_id = f"python-mqtt-{random.randint(0, 1000)}"
        self._client = self._connect()
        if self._client is not None:
            self._client.loop_start()

    def _connect(self):
        def on_connect(_client, _userdata, _flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self._client_id)
        client.on_connect = on_connect
        try:
            client.connect(self._broker, self._port)
        except Exception:
            client = None
            print("\033[91m\033[1m[ERROR]\033[0m\033[1m Failed to connect to MQTT Broker\033[0m")
            print("Communication between the vision module and the controller will \033[1mnot\033[0m work properly!")
        return client

    def register_connect_callback(self, callback):
        self._client.on_connect = callback

    def is_connected(self) -> bool:
        return self._client is not None and self._client.is_connected() is True

    def publish(self, info="you forgot the information, silly", topic=""):
        if self._client is None:
            print("MQTT Client is not connected")
            return
        try:
            if topic == "":
                topic = self._topic
            result = self._client.publish(topic, info)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{info}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
        except Exception as ex:
            print(ex)
