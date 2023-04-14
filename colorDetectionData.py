import numpy as np
import conv_utils
import cv2


class ColorDetectionData:
    def __init__(self):
        self._color_mask = np.zeros((480, 640, 3), np.uint8)

        self._hsv__lower_color = np.array([0, 0, 0])
        self._rgb__lower_color = np.array([0, 0, 0])

        self._hsv__upper_color = np.array([0, 0, 0])
        self._rgb__upper_color = np.array([0, 0, 0])

        self._rgb__picked_color = np.array([0, 0, 0])
        self._hsv__picked_color = np.array([0, 0, 0])

        self._s_range = 60
        self._v_range = 60

    def _calc_color_bounds(self, hsv__frame):
        hsv_color = self._hsv__picked_color

        # Define the lower and upper bounds of the color
        s_range = self._s_range
        v_range = self._v_range

        lower_s = 0 if hsv_color[1] - s_range < 0 else hsv_color[1] - s_range
        upper_s = 255 if hsv_color[1] + \
            s_range > 255 else hsv_color[1] + s_range
        lower_v = 0 if hsv_color[2] - v_range < 0 else hsv_color[2] - v_range
        upper_v = 255 if hsv_color[2] + \
            v_range > 255 else hsv_color[2] + v_range

        # Update the color mask to highlight only the pixels in the selected color
        self._hsv__lower_color = np.array([hsv_color[0]-10, lower_s, lower_v])
        self._hsv__upper_color = np.array([hsv_color[0]+10, upper_s, upper_v])
        self._color_mask = cv2.inRange(
            hsv__frame, self._hsv__lower_color, self._hsv__upper_color)

    @property
    def color_mask(self):
        return self._color_mask

    @property
    def rgb__lower_color(self):
        return self._rgb__lower_color

    @property
    def rgb__upper_color(self):
        return self._rgb__upper_color

    @property
    def rgb__picked_color(self):
        return self._rgb__picked_color

    def handle_color_pick(self, rgb__color, hsv__frame):
        self._rgb__picked_color = rgb__color
        self._hsv__picked_color = conv_utils.rgb_to_hsv(rgb__color)
        self._calc_color_bounds(hsv__frame)
