import cv2
import numpy as np

from flask import Flask, Response, render_template, request
from source import Source
from yolo import load_model

app = Flask(__name__)
yolo = load_model()

def gen(inference, source):
    while True:
        success, frame = next(source.frames())
        if success:
            if inference > 0:
                frame = yolo(frame)
                frame = np.squeeze(frame.render())

            _, encoded_frame = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')

@app.route('/feed/<inference>/<path:source_url>', methods=['GET'])
def video_feed(inference=0, source_url=0):
    return Response(gen(int(inference), Source(source_url)), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)