
# Augmentation of Annotation

Repo will augment annotated images which are of yolo format

prerequisite

- pip install imgaug
- pip install opencv-contrib-python
- all the image file and text files should be in a folder
- all images should be in 'jpeg' format and annotaion should be in 'txt' format

change input_folder and output_folder in image_augment.py

`python image_augment.py`

Augmentation list
- flip
- blur
- noise
- multiply
