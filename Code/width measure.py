# https://github1s.com/snsharma1311/object-size/tree/master

from scipy.spatial.distance import euclidean
from imutils import perspective
import numpy as np
import cv2

# Function to show array of images (intermediate results)
def show_images(images):
    for i, img in enumerate(images):
        cv2.imshow("image_" + str(i), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\933 label.png"
img_path = "C:\\Users\\ashis\\OneDrive\\Desktop\\data\\data_label\\train_actual_label\\101.png"

# Read binary image
binary_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Find contours in the binary image
cnts, _ = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours from left to right as leftmost contour is reference object
cnts = sorted(cnts, key=cv2.contourArea)

# Reference object dimensions
# Here for reference, I have used a 2cm x 2cm square
ref_object = cnts[0]
box = cv2.minAreaRect(ref_object)
box = cv2.boxPoints(box)
box = np.array(box, dtype="int")
box = perspective.order_points(box)
(tl, tr, br, bl) = box
dist_in_pixel = euclidean(tl, tr)
dist_in_cm = 2
pixel_per_cm = dist_in_pixel / dist_in_cm

# Draw remaining contours
for cnt in cnts:
    box = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    cv2.drawContours(binary_image, [box.astype("int")], -1, (255, 255, 255), 2)
    mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0]) / 2), tl[1] + int(abs(tr[1] - tl[1]) / 2))
    mid_pt_vertical = (tr[0] + int(abs(tr[0] - br[0]) / 2), tr[1] + int(abs(tr[1] - br[1]) / 2))
    width = euclidean(tl, tr) / pixel_per_cm
    height = euclidean(tr, br) / pixel_per_cm
    # cv2.putText(binary_image, "{:.1f}cm".format(width), (int(mid_pt_horizontal[0] - 5), int(mid_pt_horizontal[1] - 10)),
                # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(binary_image, "{:.1f}cm".format(height), (int(mid_pt_vertical[0] -200), int(mid_pt_vertical[1]-20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

show_images([binary_image])
