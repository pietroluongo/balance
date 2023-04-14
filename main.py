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
    cv2.moveWindow("RGB + Bounds", 1920-210-5, 0)

def draw_virtual_field():
    # Create a black image
    field = np.zeros((480, 640, 3), np.uint8)
    # field = Camera.bgr__frame

    def draw_field_bounds():
        cv2.line(field, (590, 50), (50, 430), (255, 0, 0), 3)
        cv2.line(field, (50, 50), (590, 430), (255, 0, 0), 3)
        cv2.rectangle(field, (50, 50), (590, 430), (0, 255, 0), 3)

    draw_field_bounds()

    ball_pos = Sim.ball.center

    if ball_pos is not None:
        cv2.circle(field, (ball_pos[0], ball_pos[1]), 10, (0, 69, 255), -1)
        cv2.putText(field, 'Ball ({}, {})'.format(ball_pos[0], ball_pos[1]), (ball_pos[0] + 10, ball_pos[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Virtual Model', field)
    cv2.moveWindow('Virtual Model', 1920-645, 1080-485)

def draw_ball_mask():
    mask =   Sim.ball.mask
    mask = cv2.resize(mask, (320, 240))
    cv2.imshow("Ball Color Mask", mask)
    cv2.moveWindow("Ball Color Mask", 645, 0)

def draw_background_mask():
    mask = Sim.background.mask
    mask = cv2.resize(mask, (320, 240))
    cv2.imshow("BG Color Mask", mask)
    cv2.moveWindow("BG Color Mask", 645, 350)

def draw_selected_colors():
    (upper, lower, picked) = Sim.ball.color_bounds
    show_selected_colors(upper, lower, picked)

def draw_composed_frame():
    cv2.imshow("Final Frame", Camera.bgr__frame)
    cv2.moveWindow("Final Frame", 1920-645, 1080-485)

def main():
    print("Hello World")
    while True:
        show_original_frame()
        Sim.tick()
        draw_composed_frame()
        draw_virtual_field()
        draw_ball_mask()
        draw_background_mask()
        draw_selected_colors()


if __name__ == '__main__':
    main()
