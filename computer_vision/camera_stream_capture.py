import cv2
import os
import time
from datetime import datetime

# List of RTSP stream URLs with folder names
# Dictionary of camera_name : RTSP_URL
# Add more cameras if required
rtsp_streams = {
'camera_robo': "rtsp://admin:avtron123@192.168.185.70:554/Streaming/Channels/101",
}


# Duration settings
capture_duration_hours = 24
capture_interval_seconds = 60  # 1 minute

# Desired image size
image_width = 1920
image_height = 1080

# Create directories for each RTSP stream if they don't exist
for camera_name in rtsp_streams.keys():
    if not os.path.exists(camera_name):
        os.makedirs(camera_name)

# Calculate the end time for capturing
start_time = time.time()
end_time = start_time + capture_duration_hours * 60 * 60

# Start capturing images
while time.time() < end_time:
    for camera_name, rtsp_url in rtsp_streams.items():
        # Create a VideoCapture object for the RTSP stream
        cap = cv2.VideoCapture(rtsp_url)

        # Check if the RTSP stream was opened successfully
        if not cap.isOpened():
            print(f"Error: Could not open RTSP stream for {camera_name}.")
            continue

        # Get the current frame
        ret, frame = cap.read()

        if ret:
            # Resize the frame to 1920x1020
            resized_frame = cv2.resize(frame, (image_width, image_height))

            # Generate a filename with the camera name, timestamp, and a unique ID
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_id = int(time.time() * 1000)  # Adding millisecond precision for uniqueness
            image_filename = f'{camera_name}_{timestamp}_{unique_id}.jpg'

            # Create the full path for saving the image in the camera's folder
            image_path = os.path.join(camera_name, image_filename)

            # Save the resized frame as an image
            cv2.imwrite(image_path, resized_frame)
            print(f"Saved image: {image_path}")
        else:
            print(f"Error: Could not read frame from {camera_name}.")

        # Release the VideoCapture object for the current stream
        cap.release()

    # Wait for 1 minute before capturing the next set of images
    time.sleep(capture_interval_seconds)

print("Image capture completed.")

