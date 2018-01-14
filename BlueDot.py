import cv2, sys, getopt, numpy as np
import ImageUtils as imu
from scipy import ndimage


def find_actin_contours(image):
    edged = cv2.Canny(image, 0, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60, 60))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    image, contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imu.display(image)
    return (image, contours)

def find_cell_contours(image):
    edged = cv2.Canny(image, 25, 175)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,1)) # (25,25) is better for Green Areas
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    image, contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return (image, contours)

def main(argv):
    argc = len(argv)
    if(argc < 1):
        print("\nError: Insufficient Arguments!")
        print("\nUsage: python3 CellCount.py [flags] <filename>")
        return -1
    image_file = argv[0]
    if '.png' not in image_file:
        print("\nError: Invalid Image Type")
        return -1

    image = cv2.imread(image_file)
    original = image.copy()

    image_cells = imu.reduce_image(image.copy(), imu.Color.B)
    image_actin = imu.reduce_image(image.copy(), imu.Color.G)

    (image_cells, contours_cells) = find_cell_contours(image_cells)
    (image_actin, contours_actin) = find_actin_contours(image_actin)

    image_cells = imu.overlay(original, contours_cells, imu.Item.Cells)
    image_actin = imu.overlay(original, contours_actin, imu.Item.Actin, area_threshold=500)

    imu.display(image_cells)
    imu.display(image_actin)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
