from camera_thread import show_original_frame
from colorDetectionData import ColorDetectionData
import cv2
import numpy as np
from sim import Sim
from camera import Camera


def show_selected_colors(rgb__upper_color, rgb__lower_color, rgb_color):
    color_image = np.zeros((210, 200, 3), np.uint8)
    color_image[:70, :] = rgb__upper_color
    color_image[70:140, :] = rgb_color[::-1]
    color_image[140:, :] = rgb__lower_color
    color_image_resized = cv2.resize(color_image, (200, 100))
    cv2.imshow("RGB + Bounds", color_image_resized)
    cv2.moveWindow("RGB + Bounds", 1290, 0)

def virtual_field():
    # Create a black image
    img = np.zeros((480, 640, 3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv2.line(img, (590, 50), (50, 430), (255, 0, 0), 3)
    cv2.line(img, (50, 50), (590, 430), (255, 0, 0), 3)
    cv2.rectangle(img, (50, 50), (590, 430), (0, 255, 0), 3)
    ball_pos = Sim.ball.center
    cv2.circle(img, (Sim.ball.center[0], Sim.ball.center[1]), 10, (0, 69, 255), -1)
    cv2.putText(img, 'Ball ({}, {})'.format(Sim.ball.center[0], Sim.ball.center[1]), (Sim.ball.center[0] + 10, Sim.ball.center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('image', img)

def main():
    print("Hello World")
    while True:
        show_original_frame()
        virtual_field()
        color_mask = Sim.ball_data.color_mask
        cv2.imshow("Ball Color Mask", color_mask)
        cv2.moveWindow("Ball Color Mask", 645, 0)
        show_selected_colors(Sim.ball_data.rgb__upper_color,
                             Sim.ball_data.rgb__lower_color, Sim.ball_data.rgb__picked_color)
        Sim.tick()
        cv2.imshow("Final Frame", Camera.bgr__frame)


if __name__ == '__main__':
    main()
