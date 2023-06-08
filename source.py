import cv2

class Source:
    def __init__(self, source_path):
        try:
            self.cap = cv2.VideoCapture(int(source_path))
        except ValueError:
            self.cap = cv2.VideoCapture(source_path)

        print("Capture Status: ", self.cap.isOpened())
    
    def frames(self):
        while True:
            yield self.cap.read()