from camera_thread import show_original_frame
from colorDetectionData import ColorDetectionData
import cv2
import numpy as np
from sim import Sim


def show_selected_colors(rgb__upper_color, rgb__lower_color, rgb_color):
    color_image = np.zeros((210, 200, 3), np.uint8)
    color_image[:70, :] = rgb__upper_color
    color_image[70:140, :] = rgb_color[::-1]
    color_image[140:, :] = rgb__lower_color
    color_image_resized = cv2.resize(color_image, (200, 100))
    cv2.imshow("RGB + Bounds", color_image_resized)
    cv2.moveWindow("RGB + Bounds", 1290, 0)


def main():
    print("Hello World")
    while True:
        show_original_frame()
        color_mask = Sim.ball_data.color_mask
        cv2.imshow("Ball Color Mask", color_mask)
        cv2.moveWindow("Ball Color Mask", 645, 0)
        show_selected_colors(Sim.ball_data.rgb__upper_color,
                             Sim.ball_data.rgb__lower_color, Sim.ball_data.rgb__picked_color)


if __name__ == '__main__':
    main()
