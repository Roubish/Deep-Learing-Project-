import cv2
from datetime import datetime

cap = cv2.VideoCapture('test_estimation.mp4')
frame_count = 0
writer = None

while True:
    ret, frame = cap.read()
    frame_count += 1
    (h, w) = frame.shape[:2]

    if writer is None:
        time = datetime.now().second
        name = "slice_" + str(time) + ".avi"
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        writer = cv2.VideoWriter(name, fourcc, 25, (w, h), True)
    if writer is not None:
        if frame_count % 100 != 0:
            writer.write(frame)
        else:
            writer.release()
            writer = None
            print (frame_count)
