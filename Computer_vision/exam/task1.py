import matplotlib.pyplot as plt
from skimage.filters import threshold_isodata, threshold_triangle
from skimage.color import rgb2gray, rgba2rgb
from skimage.measure import regionprops, label
import numpy as np

def get_binary_image(gray_image):
    iso_thresh = threshold_isodata(gray_image)
    triangle_thresh = threshold_triangle(gray_image)
    binary = np.logical_or(gray_image.copy() <= iso_thresh, gray_image.copy() >= triangle_thresh)
    return binary

def find_obj(labeled, regions):
    max_area = -float("inf")
    label = None

    for i in range(len(regions)):
        area = regions[i].area - regions[i].perimeter
        if area > max_area:
            label = regions[i].label
            max_area = area

    return (label, max_area)

if __name__ == "__main__":
    image = plt.imread("C:/#AllNeeds/Учеба/Компьютерное зрение/#Материалы к коду/task1.png")
    gray_image = rgb2gray(rgba2rgb(image))

    binary = get_binary_image(gray_image)

    labeled = label(binary)
    regions = regionprops(labeled)

    max_area_label, max_area = find_obj(labeled, regions)

    plt.subplot(121)
    plt.imshow(binary)

    if max_area_label is None:
        print("Nothing found")
    else:    
        labeled = labeled == max_area_label
        
        plt.subplot(122)
        plt.imshow(labeled)

    plt.show()