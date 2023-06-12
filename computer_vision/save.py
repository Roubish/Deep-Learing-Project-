import cv2
import os

RTSP_URL = ['rtsp://admin:assert%40123@192.168.0.203:554/h265/main/ch0/main/av_stream',
            'rtsp://admin:assert%40123@192.168.0.202:554/h265/main/ch1/main/av_stream',
            'rtsp://admin:assert%40123@192.168.0.202:554/h265/main/ch2/main/av_stream']

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'


for i, rtsp in enumerate(RTSP_URL):
    cap = cv2.VideoCapture(rtsp, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        print('Cannot open RTSP stream')
        
    while True:
        ret, frame = cap.read()
        if ret:
            file_name = str(i)+'.jpg'
            cv2.imwrite(file_name, frame)
            print(f"file saved {file_name}")
        break
        
    cap.release()
  
  
  
  
  
  
  
  
  
  
  
  '''  
    192.168.1.2











rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/101/?transportmode=unicast



rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/601/?transportmode=unicast


rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/501/?transportmode=unicast



rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/401/?transportmode=unicast



rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/301/?transportmode=unicast



rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/201/?transportmode=unicast


rtsp://admin:assert%40123@192.168.1.31:554/streaming/channels/201/?transportmode=unicast

rtsp://admin:12345scw@192.168.1.210:554/cam/realmonitor?channel=1&subtype=1

rtsp://admin:assert%40123@192.168.1.31:554/h265/main/201/main/av_stream

'''
