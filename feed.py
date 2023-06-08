import cv2
import numpy as np

from flask import Flask, Response, render_template, request
from source import Source
from yolo import load_model

from ultralyticsplus import render_result


app = Flask(__name__)
yolo = load_model()

def gen(inference, source, size):
    size = (size, size)
    #stride, names, pt = yolo.stride, yolo.names, yolo.pt
    #imgsz = check_img_size(size, s=stride)

    while True:
        success, frame = next(source.frames())
        if success:
            if inference > 0:
                result = yolo.predict(frame)
                rnd = render_result(image=frame, model=yolo, result=result[0])
                frame = np.squeeze(np.array(rnd))

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