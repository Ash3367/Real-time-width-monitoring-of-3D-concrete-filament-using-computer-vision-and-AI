import cv2
import os

# Specify the directory containing your images
image_dir = "C:\\Users\\ashis\\OneDrive\\Desktop\\annotation\\validate"

# Loop through all files in the directory
for filename in os.listdir(image_dir):
  # Check if it's an image file
  if filename.endswith((".jpg", ".png", ".jpeg")):
    # Load the image
    image = cv2.imread(os.path.join(image_dir, filename))

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image with the original filename
    new_filename = os.path.join(image_dir, filename)
    cv2.imwrite(new_filename, gray_image)

    print(f"Converted image: {filename}")

print("All images converted to grayscale!")
