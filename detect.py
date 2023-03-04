import os
import shutil
import cv2
import pafy
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# results = model("https://ultralytics.com/images/bus.jpg" ,save=True)

def check_directory():
    if os.listdir('./detect_images'):
        shutil.rmtree('./detect_images')
        os.mkdir('./detect_images')

def get_images():
    id = 1
    url = "https://www.youtube.com/watch?v=3CmwLOgQxIY"
    dir_path = "./detect_images"
    ext = 'jpg'
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    cap = cv2.VideoCapture(best.url)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, str(id))
    ret, frame = cap.read()
    cv2.imwrite('{}.{}'.format(base_path, ext), frame)

check_directory()
get_images()