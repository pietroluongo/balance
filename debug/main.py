import signal
from gui.gui import draw_all
from comms.mqtt_sender import Sender

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    try:
        _sender = Sender()
    except Exception:
        print("\033[91m\033[1m[ERROR]\033[0m\033[1m Failed to connect to MQTT Broker\033[0m")
        return
    draw_all()


if __name__ == "__main__":
    main()
