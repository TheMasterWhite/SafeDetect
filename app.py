from flask import Flask, request, jsonify
from ultralytics import YOLO
from ProcessServer import Producer, Consumer
import logging, json, queue, utils

# 配置 logging
logging.basicConfig(filename = "Logs/app.log", level = logging.INFO)
logging.basicConfig(filename = "Logs/app.log", level = logging.ERROR)

app = Flask(__name__)

dataQueue = queue.Queue()
producer = Producer(dataQueue)

# 声明模型
exhaustFanModel = None
gasTankModel = None
gasTeeModel = None
regulatorModel = None


# 检测请求接口
@app.route('/Detect', methods = ['POST'])
def Detect():
    try:
        returnObj = {"Code": 200,
                     "msg": "OK"}
        requestData = request.json
        requestId = requestData.get("requestId")
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]成功接收检测请求,requestId = " + str(requestId))
        producer.PutData(requestData)

    except Exception as e:
        curTime = utils.GetTime()
        requestData = request.json
        logging.error(f"[{curTime}]" + str(e))
        returnObj = {"Code": 400,
                     "msg": str(e)}

    finally:
        return jsonify(returnObj)


@app.route('/test', methods = ['POST'])
def test():
    returnObj = {"Code": 200}
    data = request.json
    requestId = data.get("requestId")
    curTime = utils.GetTime()
    logging.info(f"[{curTime}]成功接收检测请求,requestId = " + str(requestId))
    return requestId


# 启动服务
def StartServer():
    app.run(debug = True, host = "0.0.0.0")


if __name__ == "__main__":
    try:
        # 加载检测排气扇模型
        exhaustFanModel = YOLO(model = "Weights/exhaustFan.pt", task = "detect")
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]排气扇检测模型加载成功!")

        # 加载检测煤气罐模型
        gasTankModel = YOLO(model = "Weights/gasTank.pt", task = "detect")
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]煤气罐检测模型加载成功!")

        # 加载三通检测模型
        gasTeeModel = YOLO(model = "Weights/gasTee.pt", task = "detect")
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]三通检测模型加载成功!")

        # 加载调压阀检测模型
        regulatorModel = YOLO(model = "Weights/regulator.pt", task = "detect")
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]调压阀检测模型加载成功!")

        consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
        consumer.start()
        StartServer()

    except Exception as e:
        curTime = utils.GetTime()
        logging.error(f"[{curTime}]" + str(e))
