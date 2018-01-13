import cv2, sys, getopt, numpy as np
from scipy import ndimage
def reduce_image(image, t=0):
    w, h, _ = image.shape
    for i in range(w):
        for j in range(h):
            colors = image[i][j]
            if(t == 0):
                image[i][j] = (colors[0], 0, 0) #BGR... seriously?
            elif(t == 1):
                image[i][j] = (0, colors[1], 0)
    return image

def find_contours(image, blur=False):
    edged = cv2.Canny(image, 0, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    image, contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return (image, contours)

def find_stress_fiber_region(image):
    green_range = ([0, 0, 0], [75, 255, 75])

def overlay(original, contours, show=True):
    id_c = 0
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(original, (x, y), (x+w+2, y+h+2), (0, 255, 0), 2)
        cv2.putText(original, str(id_c), (x-5, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 255)
        id_c += 1
    cv2.imshow("Image", original)
    cv2.waitKey(0)

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
    image_cells = reduce_image(image.copy(), t=0)
    image_actin = reduce_image(image.copy(), t=1)

    (image_cells, contours_cells) = find_contours(image_cells)
    (image_actin, contours_actin) = find_contours(image_actin, blur=True)

    #overlay(original.copy(), contours_cells, show=False)
    overlay(original.copy(), contours_actin)
    

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
