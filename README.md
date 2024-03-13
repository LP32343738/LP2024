# LP2024

LP-2024 dataset offers 33,240 labeled license plates in 17,789 images. The images were taken at different time of the day, under various traffic and weather conditions, and by using different types of cameras. The size of LPs varies from as small as 32 (8x4) pixels to 3,281,900 (1850x1774) pixels.

The annotations in LP-2024 combine the positive aspects of well-annotated databases such as CCPD and AOLP. The LP-2024 database includes bounding boxes for all license plates larger than the 30-pixel threshold, below which the human eye cannot distinguish license plates from background noise. If the alphanumeric content of a license plate can be clearly read by the human eye, it is classified as readable; otherwise, it is classified as unreadable. In practical applications, readable license plates are used for LPDR research, while unreadable ones are used for LPD or deblurring methods. As shown in the image below, the license plate in the yellow box is classified as readable, while the one in the pink box is classified as unreadable.
![LP2024_read](https://github.com/LP32343738/LP2024/assets/162530571/4f20fded-4b62-4b55-ade4-56ed1c1a3c8b)

<img src="![LP2024_read](https://github.com/LP32343738/LP2024/assets/162530571/4f20fded-4b62-4b55-ade4-56ed1c1a3c8b)" alt="Your Image" width="300" height="200">

- Samples in the "readable" category include not only the alphanumeric content of the license plate (composed of numbers and letters) but also the coordinates of the four bounding boxes.
- For unreadable or occluded license plates, only the corresponding bounding box is provided without the alphanumeric content.
- License plates with occlusions below 50% of their area and with unidentifiable content are labeled as unreadable.
- License plates with content that cannot be uniquely identified are classified as unreadable regardless of individual alphanumeric values.
- License plates with occlusions exceeding 50% of their original area are ignored and not classified into either category.

However, these two categories have different types of labels. The labels for readable license plates include:

1. A sequence of 5-7 alphanumeric values representing the license plate content.
2. Bounding box of the license plate defined by the lower-left and upper-right endpoints in pixel coordinates.
3. Bounding box defined by the four vertices determining the exact area of the license plate.

The labels for unreadable license plates only include the points mentioned above in 2 and 3.


More detailed introduction of LP2024 can be found in the paper.

Some examples from the dataset are shown below:

Download Link
-
[LP-2024 Syn Download Link](https://drive.google.com/file/d/1vhWqmYkz1Bunh5isd3DyW3NQreGRBXVv/view?usp=drive_link)
\\
[LP-2024 Download Link](https://drive.google.com/file/d/1s9mDic1B7VYrhXKLDjam_a7lXdTPEHK1/view?usp=drive_link)
