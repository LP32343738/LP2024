# LP-2024 Datasets

The License Plate 2024 (LP-2024) dataset offers 33,240 license plates in 17,789 images. The images were taken across the bustling city of Taipei and neighboring towns at different times of the day, under various traffic and weather conditions, and by using different types of cameras. The size of LPs varies from as small as 4$\times$8 pixels with unrecognizable characters to 1850$\times$1774 pixels. The orientation varies from $-80^\circ\sim80^\circ$ in yaw, $-20^\circ\sim50^\circ$ in pitch, and $-60^\circ\sim 60^\circ$ in roll. A distinctive characteristic of this dataset is that 60$\%$ (10,538) images contain more than 2 LPs, and the average is 1.87 LPs per image, making LP-2024 different from almost all other datasets that have only one LP per image. Unlike most datasets annotated with rectangle bounding boxes, each LP in the LP-2024 is annotated with the coordinates of the four vertices/corners. 

Due to the in-the-wild collection of the data, many license plates are too small or too blurry for human annotators to recognize, and are hence labeled as \textit{unreadable}. There are 34,189 unreadable license plates in the LP-2024, versus the aforementioned 33,240 \textit{readable} plates. Although the unreadable license plates are excluded when considering recognition (LPR), they are a crucial part of the benchmark when considering detection (LPD), deblurring, and data augmentation. 

As shown in the image below, the license plate in the green box is classified as readable, while the one in the red box is classified as unreadable.
![LP2024_read](https://github.com/LP32343738/LP2024/assets/162530571/916098bf-783f-44fe-87cd-c4a7a1acf8e4)

We divided the data into three subsets for training (26,881 images, 40\%), validation (6,756 images, 10\%), and testing (33,792 images, 50\%) according to the attributes of the license plates, making the attribute distribution of each subset similar. The attributes include size, orientation, and illumination condition of the plates. The training set comprises 13,243 readable plates and 13,638 unreadable plates, the validation set has 3,340 readable plates and 3,416 unreadable plates, and the testing set consists of 16,657 readable plates and 17,135 unreadable plates.



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
\
[LP-2024 Download Link](https://drive.google.com/file/d/1ZmW0wFJZnvLamzdFMKWf8kiDqvlUGVGn/view?usp=sharing)
\
\
We also provide the YOLO data format to facilitate users in training YOLO-related models.
\
[LP-2024-Yolo Download Link](https://drive.google.com/file/d/1FmWP3sanNn2Beohib6FbB-ZSGgaYazTj/view?usp=sharing)
