# heldet

# Diagram

![diagram](diagram.png)

# Installation

```sh
$ virtualenv venv
$ pip install -r requirements.txt
$ python feed.py
```

# Usage

- open `http://localhost:5000` on browser
- from webcam

  - normal frame from webcam
    - http://localhost:5000/feed/0/0
  - inferenced frame from webcam
    - http://localhost:5000/feed/1/0

- from video feed
  - normal frame from video feed
    - http://localhost:5000/feed/0/<FEED_URL>
  - inferenced frame from video feed
    - http://localhost:5000/feed/1/<FEED_URL>
