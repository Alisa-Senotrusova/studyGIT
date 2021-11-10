import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from scipy.ndimage import morphology

def count(image, mask):
  erosion = morphology.binary_erosion(image, mask)
  dilation = morphology.binary_dilation(erosion, mask)
  image -= dilation
  count = label(dilation).max()
  return count

image = np.load('C:/#AllNeeds/Учеба/Компьютерное зрение/Подсчет количества объектов/ps.npy')

array_mask = np.array([
                  np.array([
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 0, 0],
                            [1, 1, 0, 0],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]
                  ]),
                  np.array([
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [0, 0, 1, 1],
                            [0, 0, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]
                  ]),
                  np.array([
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1]
                  ]),
                  np.array([
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1]
                  ])
], dtype=object)

total_count = 0
i = 1
for mask in array_mask:
  type_count = count(image, mask)
  total_count += type_count
  print(f'Type {i}:', type_count)
  i += 1
print('Total:', total_count)