from wsgiref.simple_server import WSGIServer
from flask import Flask, request, jsonify
from ultralytics import YOLO
from ProcessServer import Producer, Consumer
import logging, json, queue, utils, Config

# 配置 logging
logging.basicConfig(filename = "Logs/server.log", level = logging.INFO)

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
    try:
        app.run(host = "0.0.0.0", port = 8888, debug = False)
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]服务启动成功")
    except Exception as e:
        raise e



if __name__ == "__main__":
    try:
        consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
        consumer.start()
        StartServer()

    except Exception as e:
        curTime = utils.GetTime()
        logging.error(f"[{curTime}]" + str(e))
