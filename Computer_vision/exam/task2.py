import matplotlib.pyplot as plt
from skimage.color import rgba2rgb, rgb2hsv, rgb2gray
from skimage.measure import regionprops, label

def max_saturated_obj(regions, hsv_image):
    max_saturation = -float("inf")
    label = None

    for i in range(len(regions)):
        row, col = tuple(map(int, regions[i].centroid))
        saturation = hsv_image[row, col][1]

        if saturation > max_saturation:
            label = regions[i].label
            max_saturation = saturation

    return (label, max_saturation)

def mask_image(src, mask):
    result = src.copy()

    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            if not mask[y, x]:
                result[y, x] = [0, 0, 0]

    return result

if __name__ == "__main__":
    image = plt.imread("C:/#AllNeeds/Учеба/Компьютерное зрение/#Материалы к коду/task2.png")
    image = rgba2rgb(image)
    gray_image = rgb2gray(image)
    hsv_image = rgb2hsv(image)

    binary = gray_image.copy()
    binary[binary > 0] = 255

    labeled = label(binary)
    regions = regionprops(labeled)

    (max_saturated_label, max_saturation) = max_saturated_obj(regions, hsv_image)

    result = mask_image(image, labeled == max_saturated_label)
    
    plt.subplot(121)
    plt.imshow(image)
    plt.subplot(122)
    plt.imshow(result)
    plt.show()