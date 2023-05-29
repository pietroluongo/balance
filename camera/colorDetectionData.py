import cv2
import numpy as np

import conv_utils
from camera import Camera


class ColorDetectionData:
    def __init__(self):
        self._hsv__color_mask = np.zeros((480, 640, 1), np.uint8)

        self._hsv__lower_color = np.array([0, 0, 0])
        self._rgb__lower_color = np.array([0, 0, 0])

        self._hsv__upper_color = np.array([0, 0, 0])
        self._rgb__upper_color = np.array([0, 0, 0])

        self._rgb__picked_color = np.array([0, 0, 0])
        self._hsv__picked_color = np.array([0, 0, 0])

        self._s_range = 60
        self._v_range = 60
        self._centroid = None
        self._bounding_box = None

    def _calc_color_bounds(self):
        hsv_color = self._hsv__picked_color

        # Define the lower and upper bounds of the color
        s_range = self._s_range
        v_range = self._v_range

        lower_s = 0 if hsv_color[1] - s_range < 0 else hsv_color[1] - s_range
        upper_s = 255 if hsv_color[1] + s_range > 255 else hsv_color[1] + s_range
        lower_v = 0 if hsv_color[2] - v_range < 0 else hsv_color[2] - v_range
        upper_v = 255 if hsv_color[2] + v_range > 255 else hsv_color[2] + v_range

        # Update the color mask to highlight only the pixels in the selected color
        self._hsv__lower_color = np.array([hsv_color[0] - 10, lower_s, lower_v])
        self._rgb__lower_color = conv_utils.hsv_to_rgb(self._hsv__lower_color)

        self._hsv__upper_color = np.array([hsv_color[0] + 10, upper_s, upper_v])
        self._rgb__upper_color = conv_utils.hsv_to_rgb(self._hsv__upper_color)

        self._hsv__color_mask = cv2.inRange(
            Camera.hsv__frame, self._hsv__lower_color, self._hsv__upper_color
        )

    def update_mask(self):
        self._hsv__color_mask = cv2.inRange(
            Camera.hsv__frame, self._hsv__lower_color, self._hsv__upper_color
        )

    def get_center_and_update_bbox(self):
        contours, _ = cv2.findContours(
            self._hsv__color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # Find the largest contour
        max_contour = None
        max_contour_area = 0

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_contour_area:
                max_contour = contour
                max_contour_area = area
        if max_contour is not None:
            moments = cv2.moments(max_contour)
            # Approximate the polygonal curves of the contour
            epsilon = 0.02 * cv2.arcLength(max_contour, True)
            approx_curve = cv2.approxPolyDP(max_contour, epsilon, True)

            # Find the convex hull of the approximated curve
            hull = cv2.convexHull(approx_curve)

            # Get the coordinates of the bounding rectangle
            x, y, w, h = cv2.boundingRect(hull)
            # Calculate the four coordinates of the rectangle
            x1, y1 = x, y
            x2, y2 = x + w, y
            x3, y3 = x + w, y + h
            x4, y4 = x, y + h

            self._bounding_box = (x1, y1, x2, y2, x3, y3, x4, y4)

            if moments["m00"] > 0:
                centroid_x = int(moments["m10"] / moments["m00"])
                centroid_y = int(moments["m01"] / moments["m00"])
                self._centroid = (centroid_x, centroid_y)
            else:
                self._centroid = None
        else:
            self._centroid = None
        return self._centroid

    @property
    def color_mask(self):
        return self._hsv__color_mask

    @property
    def bounding_box(self):
        return self._bounding_box

    @property
    def rgb__lower_color(self):
        return self._rgb__lower_color

    @property
    def rgb__upper_color(self):
        return self._rgb__upper_color

    @property
    def rgb__picked_color(self):
        return self._rgb__picked_color

    def handle_color_pick(self, rgb__color):
        print(f"Picked color: {rgb__color}")
        self._rgb__picked_color = rgb__color
        self._hsv__picked_color = conv_utils.rgb_to_hsv(rgb__color)
        self._calc_color_bounds()
