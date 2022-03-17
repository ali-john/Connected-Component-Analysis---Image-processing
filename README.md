# Connected-Component-Analysis- Image-processing
---

<br>Connected Component Analysis or Labelling enables us to detect different objects from a binary image. Once different objects have been detected, we can perform a number of operations on them: from counting the number of total objects to counting the number of objects that are similar, from finding out the biggest object of the bunch to finding out the smallest and from finding out the closest pair of objects to finding out the farthest etc 
## Algorithm 
---


- Process the image from left to right.
  - If the next pixel to process is 1
    - If only one from top or left is 1, copy its label.
    - If both top and left are one and have the same label, copy it.
    - If top and left they have different labels
      - Copy the smaller label
      - Update the equivalence table.
    - Otherwise, assign a new label.
  -  Re-label with the smallest of equivalent labels
