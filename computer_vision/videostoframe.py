
import cv2
import os
import time


IMAGES_PATH = '/home/ghost/Downloads/car_dataset/image1/'
VIDEO_PATH = 'videoplayback_1.mp4'
image = 'image'


cap = cv2.VideoCapture(VIDEO_PATH)
print('Collecting images for {}', format('video2'))


i=0
while(cap.isOpened()):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
    if ret == False:
        break
    imgname = os.path.join(IMAGES_PATH,image + str(i)+'.jpg')
    cv2.imwrite(imgname,frame)
    cv2.imshow('frame',frame)
    i+=1
    cf = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1 
    cap.set(cv2.CAP_PROP_POS_FRAMES, cf+30)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    
cap.release()
cv2.destroyAllWindows()
'''

import os 
path = os.chdir('/home/ghost/Documents/image/')
i = 0
for file in os.listdir(path):
    new_file_name = "image-{}.jpeg".format(i)
    os.rename(file, new_file_name)
    i = i +1

'''
