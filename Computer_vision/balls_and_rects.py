import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import regionprops, label
import math


def get_colors(hsv_image):
    unique_vals = np.unique(hsv_image[:, :, 0])
    
    colors = []
    dist = 0
    start_idx = 0
    
    epsilon = np.diff(unique_vals).mean()
    
    for i in range(1, unique_vals.shape[0]):
        d = abs(unique_vals[i] - unique_vals[i - 1])
        if abs(dist - d) > epsilon:
            dist = 0
            colors.append(unique_vals[start_idx:i].mean() * 360)
            start_idx = i
            
    colors.append(unique_vals[start_idx:].mean() * 360)
    return colors

def count_figures(region):
    center_row, center_col = map(int, region.centroid)
    color_figures = hsv_image[center_row, center_col, 0] * 360
    color_figures = math.trunc(color_figures)

    if color_figures < (colors[0] + colors[1]) / 2:
        return 'red'
    if color_figures < (colors[1] + colors[2]) / 2:
        return 'yellow'
    if color_figures < (colors[2] + colors[3]) / 2:
        return 'green'
    if color_figures < (colors[3] + colors[4]) / 2:
        return 'turquoise'
    if color_figures < (colors[4] + colors[5]) / 2:
        return 'blue'
    if color_figures < (colors[5] + 360) / 2:
        return 'purple'
    return 'red'


image = plt.imread('C:/#AllNeeds/Учеба/Компьютерное зрение/#Материалы к коду/balls_and_rects.png')
hsv_image = color.rgb2hsv(image)

binary = np.sum(image, 2)
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

colors = get_colors(hsv_image)[1:]

rect_figures = {
    'red': 0,
    'yellow': 0,
    'green': 0,
    'turquoise': 0,
    'blue': 0,
    'purple': 0
}
circle_figures = {
    'red': 0,
    'yellow': 0,
    'green': 0,
    'turquoise': 0,
    'blue': 0,
    'purple': 0
}

for region in regions:
    res = count_figures(region)
    if np.all(region.image):
        rect_figures[res] += 1
    else:
        circle_figures[res] += 1

print('total_figures', labeled.max())
print('rect_figures', rect_figures)
print('circle_figures', circle_figures)
