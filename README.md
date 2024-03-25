# LP-2024 Datasets

LP-2024 datasets offers 33,240 labeled license plates in 17,789 images. The images were taken at different time of the day, under various traffic and weather conditions, and by using different types of cameras. The size of LPs varies from as small as 32 (8x4) pixels to 3,281,900 (1850x1774) pixels.

The annotations in LP-2024 combine the positive aspects of well-annotated databases such as CCPD and AOLP. The LP-2024 database includes bounding boxes for all license plates larger than the 30-pixel threshold, below which the human eye cannot distinguish license plates from background noise. If the alphanumeric content of a license plate can be clearly read by the human eye, it is classified as readable; otherwise, it is classified as unreadable. In practical applications, readable license plates are used for LPDR research, while unreadable ones are used for LPD or deblurring methods. As shown in the image below, the license plate in the green box is classified as readable, while the one in the red box is classified as unreadable.
![LP2024_read](https://github.com/LP32343738/LP2024/assets/162530571/916098bf-783f-44fe-87cd-c4a7a1acf8e4)


- Samples in the "readable" category include not only the alphanumeric content of the license plate (composed of numbers and letters) but also the coordinates of the four bounding boxes.
- For unreadable or occluded license plates, only the corresponding bounding box is provided without the alphanumeric content.
- License plates with occlusions below 50% of their area and with unidentifiable content are labeled as unreadable.
- License plates with content that cannot be uniquely identified are classified as unreadable regardless of individual alphanumeric values.
- License plates with occlusions exceeding 50% of their original area are ignored and not classified into either category.

However, these two categories have different types of labels. The labels for readable license plates include:

1. A sequence of 5-7 alphanumeric values representing the license plate content.
2. Bounding box defined by the four vertices determining the exact area of the license plate.

The labels for unreadable license plates only include the points mentioned above in 2.


More detailed introduction of LP2024 can be found in the paper.

Some examples from the dataset are shown below:
![LP2024_sample](https://github.com/LP32343738/LP2024/assets/162530571/ac2a3fc2-d3e0-439e-b2dc-5708dcf3f975)


Download Link
-
We are temporarily releasing 300 images each for the LP-2024-Syn test set, LP-2024 LPD, and LPR. The complete dataset will be made available after the paper is accepted.
\
[LP-2024 Syn Download Link](https://drive.google.com/file/d/1NjzTVPxhejzuHmmOhE2LBIqi26qWhP1H/view?usp=sharing)
\
[LP-2024 Download Link](https://drive.google.com/file/d/1ZmW0wFJZnvLamzdFMKWf8kiDqvlUGVGn/view?usp=sharing)
\
We also provide the YOLO data format to facilitate users in training YOLO-related models.
\
[LP-2024-Yolo Download Link](https://drive.google.com/file/d/1FmWP3sanNn2Beohib6FbB-ZSGgaYazTj/view?usp=sharing)
