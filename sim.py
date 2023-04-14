from colorDetectionData import ColorDetectionData
from camera import Camera


class Sim:
    def __init__(self):
        self._ball_data = ColorDetectionData()
        self._background_data = ColorDetectionData()

    def set_ball_color(self, rgb__color):
        self._ball_data.handle_color_pick(rgb__color, Camera.hsv__frame)

    def set_background_color(self, rgb__color):
        self._background_data.handle_color_pick(rgb__color, Camera.hsv__frame)

    @property
    def ball_data(self):
        return self._ball_data

    @property
    def background_data(self):
        return self._background_data


Sim = Sim()
