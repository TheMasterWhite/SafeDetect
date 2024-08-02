from flask import Flask, request, jsonify
from ultralytics import YOLO
import logging, json

# 配置 logging
logging.basicConfig(filename = "Logs/app.log", level = logging.ERROR)

app = Flask(__name__)


def YoloInterface(source):
    result = gasTankModel(source = source)
    a = result[0].tojson()
    return a


# 检测接口请求
@app.route("/testDetect", methods = ["POST"])
def testDetect():
    returnObj = {"Code": 200}

    try:
        data = request.json
        requestId = data.get("requestId")
        imageUrl = data.get("imageUrl")
        returnUrl = data.get("returnUrl")
        type = data.get("type")
        saveImage = data.get("saveImage", False)
        saveText = data.get("saveText", False)
        return YoloInterface(imageUrl)

    except Exception as e:
        logging.error(str(e))
        return json.dumps(str(e))

    # finally:
    #     logging.info("Received request success!")
    #     return returnObj


# 启动服务
def StartServer():
    app.run(debug = True, host = "0.0.0.0")


if __name__ == "__main__":
    try:
        # 加载检测排气扇模型
        exhaustFanModel = YOLO(model = "Weights/ExhaustFan.pt", task = "detect")
        logging.info("排气扇检测模型加载成功!")

        # 加载检测煤气罐模型
        gasTankModel = YOLO(model = "Weights/GasTank.pt", task = "detect")
        logging.info("煤气罐检测模型加载成功!")

        # 加载三通检测模型
        gasTeeModel = YOLO(model = "Weights/GasTee.pt", task = "detect")
        logging.info("三通检测模型加载成功!")

        # 加载调压阀检测模型
        regulatorModel = YOLO(model = "Weights/Regulator.pt", task = "detect")
        logging.info("调压阀检测模型加载成功!")

        StartServer()

    except Exception as e:
        logging.error(str(e))
