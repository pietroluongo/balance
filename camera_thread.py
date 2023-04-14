from camera import Camera
from colorDetectionData import ColorDetectionData
import cv2
from conv_utils import bgr_to_rgb
from sim import Sim


def mouse_callback(event, x, y, flags, param):
    bgr_color = Camera.bgr__frame[y, x]
    rgb_color = bgr_to_rgb(bgr_color)
    Sim.set_ball_color(rgb_color)
    # ColorDetectionData.handle_color_pick(rgb_color, Camera.hsv__frame)


def show_original_frame():
    cv2.imshow("Original Frame", Camera.next_frame())
    cv2.moveWindow("Original Frame", 0, 0)
    cv2.setMouseCallback("Original Frame", mouse_callback)
    cv2.waitKey(1)


def camera_thread(windowTitle="Camera"):
    while True:
        show_original_frame()
        color_mask = ColorDetectionData.get_color_mask()
        cv2.imshow("Color Mask", color_mask)
        cv2.moveWindow("Color Mask", 645, 0)
