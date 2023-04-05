import cv2
import numpy as np

# Set up the video capture
cap = cv2.VideoCapture(0)

# Initialize the color mask and centroid
color_mask = None
centroid = None

# Define the callback function for the mouse event
def mouse_callback(event, x, y, flags, param):
    global color_mask, lower_color, upper_color

    if event == cv2.EVENT_LBUTTONUP:
        # Get the color of the pixel at the clicked location
        bgr_color = frame[y, x]
        # Convert the color from BGR to HSV
        hsv_color = cv2.cvtColor(np.array([[bgr_color]], dtype=np.uint8), cv2.COLOR_BGR2HSV)[0][0]
        # Print the HSV values of the color
        print("Selected color: HSV" + str(hsv_color))

        # Update the color mask to highlight only the pixels in the selected color
        lower_color = np.array([hsv_color[0]-10, 50, 50])
        upper_color = np.array([hsv_color[0]+10, 255, 255])
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Convert the color from BGR to RGB
        rgb_color = (int(bgr_color[2]), int(bgr_color[1]), int(bgr_color[0]))
        # Print the RGB values of the color
        print("Selected color: RGB" + str(rgb_color))
        print('\n')
        # Convert the lower and upper colors from HSV to RGB
        lower_color_rgb = cv2.cvtColor(np.array([[lower_color]], dtype=np.uint8), cv2.COLOR_HSV2RGB)[0][0][::-1]
        upper_color_rgb = cv2.cvtColor(np.array([[upper_color]], dtype=np.uint8), cv2.COLOR_HSV2RGB)[0][0][::-1]

        # Display the selected color, lower color, and upper color in a single window
        color_image = np.zeros((210, 200, 3), np.uint8)
        color_image[:70, :] = upper_color_rgb
        color_image[70:140, :] = rgb_color[::-1]
        color_image[140:, :] = lower_color_rgb
        color_image_resized = cv2.resize(color_image, (200, 100))
        cv2.imshow("RGB", color_image_resized)
        cv2.moveWindow("RGB", 1290, 0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Apply the color mask to highlight only the pixels in the selected color
    if color_mask is not None:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv_frame, lower_color, upper_color)
        color_image = cv2.bitwise_and(frame, frame, mask=color_mask)

        # Find the contours of the mask
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour
        max_contour = None
        max_contour_area = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_contour_area:
                max_contour = contour
                max_contour_area = area

        # Calculate the centroid of the largest contour
        if max_contour is not None:
            moments = cv2.moments(max_contour)
            if moments["m00"] > 0:
                centroid_x = int(moments["m10"] / moments["m00"])
                centroid_y = int(moments["m01"] / moments["m00"])
                centroid = (centroid_x, centroid_y)
            else:
                centroid = None
        else:
            centroid = None

    # Draw a circle at the centroid position
    if centroid is not None:
        cv2.circle(frame, centroid, 5, (250, 95, 237), -1)

    # Display the color mask and the original frame in two windows
    if color_mask is not None:
        cv2.imshow("Color Mask", color_image)
        cv2.moveWindow("Color Mask", 645, 0)
    cv2.imshow("Original", frame)
    cv2.moveWindow("Original", 0, 0)

    # Set up the mouse callback function
    cv2.setMouseCallback("Original", mouse_callback)

    # Check for user input to exit the program
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

