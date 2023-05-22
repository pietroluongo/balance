from mqtt_sender import Sender
from gui.gui import draw_set_motor_position_window

def main():
    _sender = Sender
    # draw_pid_params_window()
    draw_set_motor_position_window()

if __name__ == "__main__":
    main()
