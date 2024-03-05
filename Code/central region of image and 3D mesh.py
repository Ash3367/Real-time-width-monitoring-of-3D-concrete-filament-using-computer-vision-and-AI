import cv2
import numpy as np
import matplotlib.pyplot as plt

def crop_center_horizontal(image, percentage=0.5):
    height, width, _ = image.shape
    # start_x = int((1 - percentage) / 8*width)
    # end_x = int((1 + percentage) / 8*width)
    start_x = width//2 - 40
    end_x = width//2 + 40
    center_horizontal_region = image[:, start_x:end_x]
    
    return center_horizontal_region

# Load your image
image_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\862_new_bw.png"  # Replace with the path to your image
original_image = cv2.imread(image_path)

# Crop the central vertical region (adjust percentage as needed)
cropped_region = crop_center_horizontal(original_image, percentage=0.6)
# ------------------------------------------------------------------------------------------------------
angle = 0  # Specify the angle of rotation (adjust as needed)
rotation_matrix = cv2.getRotationMatrix2D((cropped_region.shape[1] // 2, cropped_region.shape[0] // 2), angle, 1)
img_rotated = cv2.warpAffine(cropped_region, rotation_matrix, (cropped_region.shape[1], cropped_region.shape[0]))

img_smooth = cv2.GaussianBlur(img_rotated, (5, 5), 0)
image_filter = cv2.bilateralFilter(img_rotated,9,180,10)
# image = cv2.medianBlur(img_rotated,3)
image_filter = cv2.cvtColor(image_filter, cv2.COLOR_BGR2GRAY)
print(image_filter.shape)
cv2.imshow("image_filter", image_filter)
# Create a 3D mesh
rows, cols = image_filter.shape
x = np.arange(0, cols, 1)
y = np.arange(0, rows, 1)
x, y = np.meshgrid(x, y)
z = image_filter/ 255.0  # Normalize pixel values to the range [0, 1]

# # Plot the 3D mesh
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Show the plot
plt.show()
# ----------------------------------------------------------------------------------------------------

# Display the original and cropped images (optional)
cv2.imshow('Original Image', original_image)
cv2.imwrite("C:\\Users\\ashis\\OneDrive\\Desktop\\cropped image.png", cropped_region)
cv2.imshow('Cropped Vertical Region', cropped_region)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now, you can perform your monitoring operations on the cropped_region
# For example, you can use OpenCV functions, machine learning models, etc.
