import sys

# import json
# from math import ceil
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# from mqtt_sender import Sender
from .slider import Slider
from .constants import WIDTH, HEIGHT


def draw_status_label(parent, is_connected):
    status_label = QLabel(parent)
    if is_connected:
        status_label.setText("Connected")
        status_label.setStyleSheet("color: rgb(0, 150, 0);")
    else:
        status_label.setText("Not Connected")
        status_label.setStyleSheet("color: rgb(255, 0, 0);")
    status_label.move(WIDTH - 100, 180)
    status_label.show()


def draw_mqtt_connection_status(parent):
    text_label = QLabel(parent)
    text_label.setText("MQTT Connection Status: ")
    text_label.move(WIDTH - 250, 180)
    text_label.show()


m1_data = 0
m2_data = 0


def send_mqtt_data():
    # sender = Sender
    # data = {
    #     "m1": ceil(m1_data * 1.8),
    #     "m2": ceil(m2_data * 1.8)
    # }
    # print(json.dumps(data))
    # sender.publish(json.dumps(data), "/balance/debug/setPosition")
    print("Clicked")


def draw_pid_params_window():
    app = QApplication(sys.argv)
    widget = QWidget()

    # text_label = QLabel(widget)
    # text_label.setText("Parâmetros do PID!")
    # text_label.move(10, 10)

    # widget.setGeometry(50, 50, WIDTH, 200)
    # widget.setWindowTitle("PID params control")
    widget.setGeometry(50, 50, WIDTH, HEIGHT)
    widget.show()

    button = QPushButton("Enviar parâmetros", widget)
    button.setToolTip("This is an example button")
    button.move(WIDTH // 2 - button.width(), 200)
    button.show()
    button.clicked.connect(send_mqtt_data)
    # draw_mqtt_connection_status(widget)
    Slider("P", widget, 30, 50)
    Slider("I", widget, 30, 100)
    Slider("D", widget, 30, 150)
    # ConnectionStatus(widget)
    sys.exit(app.exec_())


def draw_set_motor_position_window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(50 + WIDTH + 10, HEIGHT, WIDTH, HEIGHT // 2)
    widget.show()

    def set_m1_val(a: float):
        global m1_data
        m1_data = a
        send_mqtt_data()

    def set_m2_val(a: float):
        global m2_data
        m2_data = a
        send_mqtt_data()

    slider_m1 = Slider("M1", widget, 30, 50)
    slider_m2 = Slider("M2", widget, 30, 100)

    slider_m1.register_update_callback(set_m1_val)
    slider_m2.register_update_callback(set_m2_val)

    button = QPushButton("Enviar valores", widget)
    button.setToolTip("This is an example button")
    button.move(WIDTH // 2 - button.width() // 2, 200)
    button.show()
    button.clicked.connect(send_mqtt_data)

    sys.exit(app.exec_())
