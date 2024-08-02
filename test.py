from flask import Flask, request, jsonify
from ultralytics import YOLO

app = Flask(__name__)
app.config['AIOHTTP_ASYNC_RUN_SIGNAL'] = True


@app.route('/detect/predict', methods = ["GET", "POST"])
def Detect():
    model = YOLO("Weights/Gas tank煤气罐/best.pt",
                 task = "detect")
    data = request.json
    source = data.get("source")
    results = model(source = source,
                    save = True)
    imgNumber = len(results)




if __name__ == '__main__':
    model = YOLO("Weights/gasTank.pt",
                 task = "detect")
    results = model("Data/1657593144.jpg")
    result = results[0]
    print(result.keypoints)