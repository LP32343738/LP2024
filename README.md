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



Data Download 
--
 1. [Get a password](#how-to-get-a-password)
 2. [Restriction](#restriction)
 3. [Download Link](#download-link)
 
How to get a Password
-
Please send an e-mail to the database administrator and cc. to Prof. Gee-Sern (Jison) Hsu to receive the passcode to unlock the zipped database. Your Email MUST be sent from a valid University account and include the following [request forms](./RequestForms.txt):

```
Subject: Application to download the LP2024 database
Name: <your first and last name>
Affiliation: <University where you work>
Department: <your department>
Current position: <your job title>
Email: <must be the email at the above mentioned institution>
Postal Address:
Phone number:
I have read and agreed to follow the restrictions specified in the LP2024 database webpage. This database will only be used for research purposes. I will not make any part of this database available to a third party. I'll not sell any part of this database or make any profit from its use.
<your signature>
```
In general, a password will take 3-7 workdays to issue. To avoid problems with our spam filter, make sure that your email is sent from an .edu (or similar) address. Failure to follow the instruction may result in no response. 

Database administrator: avlabdba@gmail.com

Prof. Hsu's e-mail: jison@mail.ntust.edu.tw



Restriction
-
To guarantee the proper use of this database, the following restrictions must be followed by any person who has downloaded the database.
 1. All submissions, publications, and works that use or talk about the LP2024 database must cite the paper. 
 2. Permission is NOT granted to reproduce or distribute the database. 
 3. Written permission must be approved by Prof. Gee-Sern Hsu if a faculty member desires to share the database with her/his co-workers or students. Even then, the database cannot be posted on a webpage accessible from outside the faculty research group. 
 4. No economical profit can be made from this database. 
 
No country or institution is excluded of any of the above restrictions. Failure to follow the restrictions will be legally prosecuted.


Download Link
-
We are temporarily releasing 400 images each for the LP-2024 LPD, and LPR. The complete dataset will be made available after the paper is accepted.

[LP-2024 Download Link](https://drive.google.com/drive/folders/1TS3UkpbfOOmXc40H6eVWc9XYHwC0taGt?usp=sharing)
\
\
[LP-2024 Syn Dataset (105.5GB)](https://drive.google.com/file/d/1NjzTVPxhejzuHmmOhE2LBIqi26qWhP1H/view?usp=sharing)

Due to the significant size of the synthetic dataset, we will be transferring it via hard drive. If you require the synthetic dataset, please contact the Database Administrator to arrange the details for hard drive delivery.



