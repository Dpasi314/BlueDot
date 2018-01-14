import cv2
from enum import Enum
class Color(Enum):
    R = 0
    G = 1
    B = 2

class Item(Enum):
    Cells = 0
    Actin = 1

def reduce_image(image_original, color, copy=False):
    image = None
    if(copy):
        image = image_original.copy()
    else:
        image = image_original
    w, h, _ = image.shape
    pixel_color = None
    if(color == Color.R):
        for i in range(w):
            for j in range(h):
                image[i][j] = (0, 0, image[i][j][2])
    elif(color == Color.G):
        for i in range(w):
            for j in range(h):
                image[i][j] = (0, image[i][j][1], 0)
    else:
        for i in range(w):
            for j in range(h):
                image[i][j] = (image[i][j][0], 0, 0)
    return image
    
def overlay(image_original, contours, item, id_items=True, area_threshold=10):
    contour_id = 0
    contour_area = None
    image = image_original.copy()
    outline_color = (0, 255, 0)
    outline_width = 2
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if(item == Item.Cells):
        for cnt in contours:
            contour_area = cv2.contourArea(cnt)
            if(contour_area > area_threshold):
                (x, y), r = cv2.minEnclosingCircle(cnt)
                x, y, r = int(x), int(y), int(r)
                cv2.circle(image, (x, y), r, outline_color, outline_width)
                cv2.putText(image, str(contour_id), (x - 25, y - 25), font, 1, 255)
                contour_id += 1

    else:
        for cnt in contours:
            contour_area = cv2.contourArea(cnt)
            if(contour_area > area_threshold):
                (x, y, w, h) = cv2.boundingRect(cnt)
                x, y, w, h = int(x), int(y), int(w), int(h)
                cv2.rectangle(image, (x, y), (x+w, y+h), outline_color, outline_width)
                cv2.putText(image, str(contour_id), (x - 25, y - 25), font, 1, 255)
                contour_id += 1

    return image

def display(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyWindow(title)




