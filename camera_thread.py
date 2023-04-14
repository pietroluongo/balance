from camera import Camera
from data import Data
import cv2
import conv_utils

def mouse_callback(event, x, y, flags, param):
    bgr_color = Camera.bgr__frame[y, x]
    rgb_color = conv_utils.bgr_to_rgb(bgr_color) # (int(bgr_color[2]), int(bgr_color[1]), int(bgr_color[0]))
    Data.handle_color_pick(rgb_color, Camera.hsv__frame)

def show_original_frame():
    cv2.imshow("Original Frame", Camera.next_frame())
    cv2.moveWindow("Original Frame", 0, 0)
    cv2.setMouseCallback("Original Frame", mouse_callback)
    cv2.waitKey(1)

def camera_thread(windowTitle = "Camera"):
    while True:
        show_original_frame()
        color_mask = Data.get_color_mask()
        cv2.imshow("Color Mask", color_mask)
        cv2.moveWindow("Color Mask", 645, 0)