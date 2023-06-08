import os
import torch
import math

from sahi import AutoDetectionModel

MODEL_YOLOV = 'ultralytics/yolov5'
MODEL_TYPE = 'custom'
MODEL_PATH = 'models/best5.pt'
MODEL_CONF = 0.5
MODEL_IOU = 0.5
MODEL_IMGSZ = (640, 640)

def make_divisible(x, divisor):
    if isinstance(divisor, torch.Tensor):
        divisor = int(divisor.max())
    return math.ceil(x / divisor) * divisor

def check_img_size(imgsz, s=32, floor=0):
    if isinstance(imgsz, int):
        new_size = max(make_divisible(imgsz, int(s)), floor)
    else:
        imgsz = list(imgsz)
        new_size = [max(make_divisible(x, int(s)), floor) for x in imgsz]
    if new_size != imgsz:
        print("WARNING imgsz")

    return new_size

def load_model():
    # model = torch.hub.load(MODEL_YOLOV,
    #                        MODEL_TYPE,
    #                        MODEL_PATH,
    #                        force_reload=True)
    model = AutoDetectionModel.from_pretrained(
        model_type='yolov5',
        model_path=MODEL_PATH,
        confidence_threshold=MODEL_CONF
    )

    return model