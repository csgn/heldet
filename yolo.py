import os
import torch
import math

from ultralyticsplus import YOLO

MODEL_YOLOV = 'WangRongsheng/BestYOLO'
MODEL_TYPE = 'custom'
MODEL_PATH = 'models/hardhat.pt'
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
    # model.conf = MODEL_CONF
    # model.iou = MODEL_IOU

    # return model
    model = YOLO('keremberke/yolov8m-hard-hat-detection')
    model.overrides['conf'] = 0.25  # NMS confidence threshold
    model.overrides['iou'] = 0.45  # NMS IoU threshold
    model.overrides['agnostic_nms'] = False  # NMS class-agnostic
    model.overrides['max_det'] = 1000  # maximum number of detections per image


    return model
