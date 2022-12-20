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

 ---
 ## Example:
 To illustrate connected components labeling, we start with a simple binary image containing some distinct artificial objects.
 
 
 ![image](https://user-images.githubusercontent.com/63426759/208630330-55ebc252-a5ac-4dca-8a57-d9cbfe501330.png)
 
 After scanning this image and labeling the distinct pixels classes with a different grayvalue, we obtain the labeled output image.
 
 ![image](https://user-images.githubusercontent.com/63426759/208630774-f06c549a-c265-477b-8e0f-86b33ddc4821.png)
 
 Note that this image was scaled, since the initial grayvalues (1 - 8) would all appear black on the screen. However, the pixels initially assigned to the lower classes (1 and 2) are still indiscernible from the background. If we assign a distinct color to each graylevel we obtain:
 
 
 ![image](https://user-images.githubusercontent.com/63426759/208631123-a1013c2b-2286-461e-bc08-93661dff6dc6.png)
 
