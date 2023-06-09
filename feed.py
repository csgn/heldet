import cv2
import numpy as np

from flask import Flask, Response, render_template, request
from source import Source
from yolo import load_model

app = Flask(__name__)
yolo = load_model()

def gen(inference, source, size):
    size = (size, size)
    while True:
        success, frame = next(source.frames())
        if success:
            if inference > 0:
                results = yolo(frame)
                frame = np.squeeze(results.render())

            _, encoded_frame = cv2.imencode('.jpg', frame)

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame.tobytes() + b'\r\n')

    del source

@app.route('/feed/<inference>/<int:size>/<path:source_url>', methods=['GET'])
def video_feed(inference=0, size=640, source_url=0):
    try:
        return Response(gen(int(inference), Source(source_url), size), 
                        200,
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        return Response(str(e), 500)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)