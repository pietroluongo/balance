from camera_thread import show_original_frame
from data import Data
import cv2
import numpy as np

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
        color_mask = Data.color_mask
        cv2.imshow("Color Mask", color_mask)
        cv2.moveWindow("Color Mask", 645, 0)
        show_selected_colors(Data.rgb__upper_color, Data.rgb__lower_color, Data.rgb__picked_color)

if __name__ == '__main__':
    main()