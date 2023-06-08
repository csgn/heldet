import os
import torch

MODEL_YOLOV = 'ultralytics/yolov5'
MODEL_TYPE = 'custom'
MODEL_PATH = 'models/best.pt'
MODEL_CONF = 0.5
MODEL_IOU = 0.5
MODEL_IMGSZ = (640, 640)

def load_model():
    model = torch.hub.load(MODEL_YOLOV,
                           MODEL_TYPE,
                           MODEL_PATH,
                           force_reload=True)
    model.conf = MODEL_CONF
    model.iou = MODEL_IOU

    return model