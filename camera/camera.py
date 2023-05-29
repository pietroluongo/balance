import cv2


class Camera:
    def __init__(self):
        self._cap = cv2.VideoCapture("http://192.168.0.101:4747/video")
        self._bgr__frame = None
        self._hsv__frame = None

    def next_frame(self):
        ret, frame = self._cap.read()
        self._bgr__frame = frame
        self._hsv__frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return frame

    @property
    def bgr__frame(self):
        return self._bgr__frame

    @property
    def hsv__frame(self):
        return self._hsv__frame


Camera = Camera()
