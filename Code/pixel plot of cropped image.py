import cv2
import numpy as np

# Load your binary image (replace this with your actual binary image)
binary_image_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\cropped image.png"
original_image = "C:\\Users\\ashis\\OneDrive\\Desktop\\862_new_bw.png"
binary_image = cv2.imread(binary_image_path, cv2.IMREAD_GRAYSCALE)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (adjust the threshold as needed)
min_contour_length = 50
filtered_contours = [cnt for cnt in contours if cv2.arcLength(cnt, closed=True) > min_contour_length]

# Draw the filtered contours on the original binary image for visualization
result_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(result_image, filtered_contours, -1, (0, 255, 0), 2)

# Measure distances between the lines
line_distances = [cv2.pointPolygonTest(cnt, (0, 0), True) for cnt in filtered_contours]

# Annotate the distances on the image
for i, distance in enumerate(line_distances):
    cv2.putText(original_image, f"Distance {i + 1}: {distance:.2f} pixels", (5, 15 + i * 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 2, cv2.LINE_AA)

# Display the annotated image with distances
cv2.imshow('Annotated Binary Image with Distances', result_image)
cv2.imshow('img', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
