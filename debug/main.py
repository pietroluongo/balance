from gui.gui import draw_all
from comms.mqtt_sender import Sender
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    _sender = Sender()
    draw_all()


if __name__ == "__main__":
    main()
