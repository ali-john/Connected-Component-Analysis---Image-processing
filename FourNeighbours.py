# Four neighbours of pixel connected component analysis of image for object counts
import numpy as np
import cv2 as opencv

v_set=255
img = opencv.imread('Picture2.png', opencv.IMREAD_GRAYSCALE)
r, c = np.shape(img)
for i in range(r):
    for j in range(c):
        if img[i, j] >= 127:
            img[i, j] = 255
        else:
            img[i, j] = 0

original_matrix = img
rows, col = original_matrix.shape
pad_rows = rows + 2
pad_col = col + 2
padded_matrix = np.zeros((pad_rows, pad_col))

for i in range(rows):
    for j in range(col):
        if original_matrix[i, j] != 0:
            padded_matrix[i + 1, j + 1] = v_set

adjacency_list = []
label = 0
label_matrix = np.zeros((pad_rows, pad_col))
# iterate padded matrix and look for 1.
for i in range(1, pad_rows - 1):
    for j in range(1, pad_col - 1):
        if (padded_matrix[i, j]) == v_set:
            # case 1 when both are zero
            if padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j] == 0:
                label = label + 1
                adjacency_list.append(label)
                label_matrix[i, j] = label
            # case 2a when left is 1
            elif padded_matrix[i, j - 1] == v_set and padded_matrix[i - 1, j] == 0:
                label_matrix[i, j] = label_matrix[i, j - 1]
            # case 2b when top is 1
            elif padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j] == v_set:
                label_matrix[i, j] = label_matrix[i - 1, j]
            # case 3 when both are 1
            elif padded_matrix[i, j - 1] == v_set and padded_matrix[i - 1, j] == v_set:
                # check if both ones have same labeled or not
                if label_matrix[i, j - 1] == label_matrix[i - 1, j]:
                    label_matrix[i, j] = label_matrix[i, j - 1]
                # if both ones have different labels
                else:
                    if label_matrix[i, j - 1] > label_matrix[i - 1, j]:
                        label_matrix[i, j] = label_matrix[i - 1, j]
                        adjacency_list[label - 1] = int(label_matrix[i - 1, j])
                    else:
                        label_matrix[i, j] = label_matrix[i, j - 1]
                        adjacency_list[label - 1] = int(label_matrix[i, j - 1])

for i in range(adjacency_list.__len__()):
    if i != adjacency_list[i] - 1:
        replaced = i + 1
        to_replace = adjacency_list[i]
        for j in range(1, pad_rows - 1):
            for k in range(1, pad_col - 1):
                if label_matrix[j, k] == replaced:
                    label_matrix[j, k] = to_replace

x = len(np.unique(adjacency_list))
print(f'Number of objects in image are {x}')

