import matplotlib.pyplot as plt
from skimage.color.colorconv import rgb2gray
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops
from skimage import morphology
import os

directory = os.listdir(path='images')
amount = 0

for file in directory:
    img = plt.imread('./images/'+file)
    gray = rgb2gray(img)
    thresh = threshold_otsu(gray)
    binary = gray < thresh
    erosion = morphology.binary_erosion(binary)
    dilation = morphology.binary_dilation(erosion)
    labeled = label(dilation)
    labeled = labeled[50:-50, 50:-50]
    regions = regionprops(labeled)
    count = 0
    for region in regions:
        if region.eccentricity > 0.99 and region.equivalent_diameter > 170:
            count += 1
    amount += count

print(amount)
