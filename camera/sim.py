import json

import cv2

from background import Background
from ball import Ball
from camera import Camera
from comms import mqtt_sender


class Sim:
    def __init__(self):
        self._ball = Ball()
        self._background = Background()

    def set_ball_color(self, rgb__color):
        self._ball.color = rgb__color

    def set_background_color(self, rgb__color):
        self._background.color = rgb__color

    @property
    def ball(self):
        return self._ball

    @property
    def background(self):
        return self._background

    def tick(self):
        self._ball.tick()
        self._background.tick()
        centroid = self._ball.center
        if centroid is not None:
            cv2.circle(Camera.bgr__frame, centroid, 5, (250, 95, 237), -1)
            mqtt_sender.Sender().publish(json.dumps(self._ball.to_json()), "/balance/ball")

        if self._background.pos is not None:
            x1, y1, x2, y2, x3, y3, x4, y4 = self._background.pos
            cv2.circle(Camera.bgr__frame, (x1, y1), 5, (1, 2, 255), -1)
            cv2.circle(Camera.bgr__frame, (x2, y2), 5, (1, 2, 255), -1)
            cv2.circle(Camera.bgr__frame, (x3, y3), 5, (1, 2, 255), -1)
            cv2.circle(Camera.bgr__frame, (x4, y4), 5, (1, 2, 255), -1)


Sim = Sim()
