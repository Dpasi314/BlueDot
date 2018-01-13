# BlueDot
BlueDot is a Python program created to help identify and count cells and stress fibers as well as determining the percentage of cells in Actin versus those that are not.

## About the Creation
Using Pillow, OpenCV and Python.

## An Example
Consider the following picture:
![B1-2.png](/images/B1-2.png)

We can see all the cells in this picture represented in Blue.

![B1-After.png](/images/B1-After.png)
We can see in the after image that we've successfully identified all of the cells in the picture.

## Current Issues and ToDo
Not all the cells are found individually. Using OpenCV, we find the contours of the image, and then draw them out, find their location and place a box around the cell or cell group. Unfortunately, because of this, we're unable to find each individual cell. 

### ToDo
Enhance the current cell finding procedure, perhaps implement some sort of machine learning. 
Optional flags to look at more than one image

