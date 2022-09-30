import glob
from math import gamma
import os
import cv2
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import imgaug.augmenters as iaa

def convert_yolo2xy(size, box):
    center_X, center_y, width, height = box[0], box[1], box[2], box[3]
    x1 = int((center_X-width/2)*size[0])
    x2 = int((center_X+width/2)*size[0])
    y1 = int((center_y-height/2)*size[1])
    y2 = int((center_y+height/2)*size[1])
    return (x1, x2, y1, y2)

def convert_xy2yolo(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def save_augmentation(augmentation_name,
                    seq,
                    orignal_img_path,
                    output_folder):

    img = cv2.imread(orignal_img_path)
    # image_height, image_width, _ = img.shape
    
    orignal_txt_path = orignal_img_path.replace('JPG', 'txt')
    
    shape = img.shape
    with open(orignal_txt_path, 'r') as txt:
        bounding_boxes = []
        for line in txt:
            clas, center_X, center_y, width, height = (float(i) for i in line.split(" "))
            x1, x2, y1, y2 = convert_yolo2xy(shape, [center_X, center_y, width, height])
            # cv2.rectangle(img, (x2, y2), (x1, y1), (255, 0, 0), 2)
            bounding_boxes.append(BoundingBox(x1=x1, x2=x2, y1=y1, y2=y2))

    bbs = BoundingBoxesOnImage(bounding_boxes, shape=shape)
    seq = iaa.Sequential([seq]) # apply horizontal flip
    image_aug, bbs_augs = seq(image=img, bounding_boxes=bbs)
    bbs_augs = bbs_augs.remove_out_of_image().clip_out_of_image()

    img_file, jpg_extn = os.path.basename(orignal_img_path).split('.')
    txt_file, txt_extn = os.path.basename(orignal_txt_path).split('.')
    image_path = os.path.join(output_folder, img_file+'_'+augmentation_name+'.'+jpg_extn)
    text_path = os.path.join(output_folder, txt_file+'_'+augmentation_name+'.'+txt_extn)

    cv2.imwrite(image_path, image_aug)
    with open(text_path, 'w') as file:
        all_lines = []
        for bbx in bbs_augs:
            box = (bbx.x1, bbx.x2, bbx.y1, bbx.y2)
            x, y, w, h = convert_xy2yolo(image_aug.shape, box)
            all_lines.append(f"{int(clas)} {round(x,6)} {round(y,6)} {round(w,6)} {round(h,6)}\n")
        file.writelines(all_lines)

def augment(img_file_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    augmentation_list = [(iaa.Fliplr(p = 1.0), 'flip'),
                        (iaa.GaussianBlur(sigma=(0, 6.0)), 'gblur'),                    
                        (iaa.Multiply((0.8, 1.2), per_channel=0.2), 'multiply')]
    
    for augmentation_seq, augmentation_name in augmentation_list:
        save_augmentation(augmentation_name,
                        augmentation_seq,
                        img_file_path,
                        output_folder)
            
if __name__=="__main__":
    # add the path to the folder with the to be augmented
    input_folder = "/home/akshay/assert/hackathon-data/sorted/grade/grade-4"
    if not os.path.exists(input_folder):
        print('input folder does not exist')
    output_folder = "/home/akshay/assert/hackathon-data/sorted/grade/grade-4/augs"

    img_file_list = glob.glob(os.path.join(input_folder, "*.JPG"))
    for img_file in img_file_list:
        print(os.path.basename(img_file))
        augment(img_file, output_folder)
