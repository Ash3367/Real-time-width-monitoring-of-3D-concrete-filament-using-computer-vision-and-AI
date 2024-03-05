import cv2
import numpy as np

# Load the image
file_name = "C:\\Users\\ashis\\OneDrive\\Desktop\\New folder\\concrete_data\\test\\2.png"
image = cv2.imread(file_name)

# Convert to HSV color space for better red filtering
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define a specific range for red intensity (adjust based on your image)
lower_red = (0, 100, 100)  # Hue, Saturation, Value
upper_red = (60, 255, 255)

# Create a mask for red pixels
yellow_mask = cv2.inRange(hsv_image, lower_red, upper_red)
cv2.imshow("yellow_mask", yellow_mask)


# cv2.imwrite("C:\\Users\\ashis\\OneDrive\\Desktop\\862_new_bw.png", final)
print(image.shape)
print(yellow_mask.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
