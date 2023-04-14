from colorDetectionData import ColorDetectionData
from camera import Camera
from ball import Ball

import cv2

class Sim:
    def __init__(self):
        self._ball_data = ColorDetectionData()
        self._ball = Ball()
        self._background_data = ColorDetectionData()

    def set_ball_color(self, rgb__color):
        self._ball_data.handle_color_pick(rgb__color, Camera.hsv__frame)

    def set_background_color(self, rgb__color):
        self._background_data.handle_color_pick(rgb__color, Camera.hsv__frame)

    @property
    def ball_data(self):
        return self._ball_data

    @property
    def ball(self):
        return self._ball

    @property
    def background_data(self):
        return self._background_data

    def tick(self):
        self._ball_data.update_mask(Camera.hsv__frame)
        centroid = self._ball_data.get_center()
        if centroid is not None:
            cv2.circle(Camera.bgr__frame, centroid, 5, (250, 95, 237), -1)
            self._ball.update_position(centroid[0], centroid[1])


Sim = Sim()
