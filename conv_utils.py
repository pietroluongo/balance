import cv2
import numpy as np


def bgr_to_hsv(bgr_color):
    return cv2.cvtColor(
        np.array([[bgr_color]], dtype=np.uint8), cv2.COLOR_BGR2HSV)[0][0]


def bgr_to_rgb(bgr_color):
    return cv2.cvtColor(
        np.array([[bgr_color]], dtype=np.uint8), cv2.COLOR_BGR2RGB)[0][0]


def rgb_to_hsv(rgb_color):
    return cv2.cvtColor(
        np.array([[rgb_color]], dtype=np.uint8), cv2.COLOR_RGB2HSV)[0][0]

def hsv_to_rgb(hsv_color):
    return cv2.cvtColor(
        np.array([[hsv_color]], dtype=np.uint8), cv2.COLOR_HSV2RGB)[0][0]