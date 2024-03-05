import os
import cv2

def convert_to_binary(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        # Read the image
        image_path = os.path.join(input_folder, image_file)
        original_image = cv2.imread(image_path)

        # Convert the image to binary
        binary_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Save the binary image with the original filename in the output folder
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, binary_image)

    print("Conversion complete.")

# Specify the input and output folders
input_folder_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\New folder\\data_label\\test_label"
output_folder_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\New folder\\binary_label\\test_label"

# Call the function to convert images to binary and save them
convert_to_binary(input_folder_path, output_folder_path)
