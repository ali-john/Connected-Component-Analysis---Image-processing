import numpy as np
import cv2 as opencv

v_set = 255
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
# Iterating padded matrix, look for v set value and update label matrix
for i in range(1, pad_rows - 1):
    for j in range(1, pad_col - 1):
        if padded_matrix[i, j] == v_set:
            # CASE 1 when upper diagonal and top and left pixel are 0
            if padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j] == 0 and padded_matrix[i - 1, j - 1] == 0 and \
                    padded_matrix[i - 1, j + 1] == 0:
                label = label + 1
                adjacency_list.append(label)
                label_matrix[i, j] = label
            # CASE 2
            # case 2a -- if left pixel is one
            elif padded_matrix[i, j - 1] == v_set and (
                    padded_matrix[i - 1, j] == 0 and padded_matrix[i - 1, j - 1] == 0 and padded_matrix[
                i - 1, j + 1] == 0):
                label_matrix[i, j] = label_matrix[i, j - 1]
            # case 2b -- if top pixel is one
            elif padded_matrix[i - 1, j] == v_set and (
                    padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j - 1] == 0 and padded_matrix[
                i - 1, j + 1] == 0):
                label_matrix[i, j] = label_matrix[i - 1, j]
            # case 2c -- if left upper diagonal is one
            elif padded_matrix[i - 1, j - 1] == v_set and (
                    padded_matrix[i - 1, j] == 0 and padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j + 1] == 0):
                label_matrix[i, j] = label_matrix[i - 1, j - 1]
            # case 2d -- if upper right diagonal is one
            elif padded_matrix[i - 1, j + 1] == v_set and (
                    padded_matrix[i - 1, j] == 0 and padded_matrix[i, j - 1] == 0 and padded_matrix[i - 1, j - 1] == 0):
                label_matrix[i, j] = label_matrix[i - 1, j + 1]
            # CASE 3 -- more than 1 neighbouring pixel is from v set
            else:
                high_list = []
                if padded_matrix[i, j - 1] == v_set:
                    high_list.append('label_matrix[i, j-1]')
                elif padded_matrix[i - 1, j - 1] == v_set:
                    high_list.append('label_matrix[i-1, j-1]')
                elif padded_matrix[i - 1, j] == v_set:
                    high_list.append('label_matrix[i-1, j]')
                elif padded_matrix[i - 1, j + 1] == v_set:
                    high_list.append('label_matrix[i-1, j+1]')
                equal = True
                x = eval(high_list[0])  # get first value use for comparison of labels
                for y in range(1, len(high_list)):
                    if eval(high_list[y]) != x:  # labels are different
                        equal = False

                if equal:  # if labels of every v set belonging element is same- assign that label
                    label_matrix[i, j] = eval(high_list[0])
                else:
                    labels_list = []
                    for a in high_list:
                        labels_list.append(eval(a))

                    label_matrix[i, j] = min(labels_list)
                    b = max(labels_list)
                    c = adjacency_list.index(b)
                    adjacency_list[c] = min(labels_list)


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
