import cv2
import os
import numpy as np

# Specify the input and output folders
input_folder = "C:\\Users\\ashis\\OneDrive\\Desktop\\New folder\\concrete_data\\train_actual"
output_folder = "C:\\Users\\ashis\\OneDrive\\Desktop\\output_folder\\train_actual_label"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):  # Adjust file extensions as needed
        # Construct the full path to the input image file
        input_file_path = os.path.join(input_folder, filename)

        # Load the input image
        image = cv2.imread(input_file_path)

        # Convert to HSV color space for better color filtering
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define a specific range for yellow intensity (adjust based on your image)
        lower_yellow = (0, 100, 100)  # Hue, Saturation, Value
        upper_yellow = (60, 255, 255)

        # Create a mask for yellow pixels
        yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Save the yellow mask with the same filename in the output folder
        output_file_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_file_path, yellow_mask)

        # Display the yellow mask for each image
        # cv2.imshow("Yellow Mask", yellow_mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
