from flask import Flask, request, jsonify
from flask_aiohttp import AioHTTP
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


@app.route("/test", methods = ["post"])
async def test():
    data = await request.json
    source = data.get("source")
    return jsonify({"Status": "Success"})


if __name__ == '__main__':
    app.run(host = '0.0.0.0',
            debug = True)
