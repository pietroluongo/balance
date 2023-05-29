from PySide6.QtWidgets import QMainWindow

from .ui.console import Ui_MainWindow

from comms import mqtt_receiver
from paho.mqtt.client import MQTTMessage
import json
class Console(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._client = mqtt_receiver.MQTTClient(topic="/balance/console", callback=self._handle_message)

    def _handle_message(self, client, userdata, msg: MQTTMessage):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        self._ui.consoleContent.append(f"[{msg.timestamp:.2f}] {msg.payload.decode()}")