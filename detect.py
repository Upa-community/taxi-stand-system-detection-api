import os
import shutil
import cv2
import pafy
from ultralytics import YOLO

def check_directory():
    if os.path.isdir("./detect_images"):
        shutil.rmtree("./detect_images")
    
    if os.path.isdir("./runs"):
        shutil.rmtree("./runs")

    os.mkdir("./detect_images")
    os.mkdir("./runs")

def get_images():
    id = 1
    url = "https://www.youtube.com/watch?v=3CmwLOgQxIY"
    dir_path = "./detect_images"
    ext = "jpg"
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    cap = cv2.VideoCapture(best.url)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, str(id))
    ret, frame = cap.read()
    cv2.imwrite('{}.{}'.format(base_path, ext), frame)

def detect_images():
    model = YOLO("yolov8n.pt")
    model("./detect_images" ,save=True)    

check_directory()
get_images()
detect_images()