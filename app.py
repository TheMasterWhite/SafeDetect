from wsgiref.simple_server import WSGIServer
from flask import Flask, request, jsonify
from ultralytics import YOLO
from ProcessServer import Producer, Consumer
import logging, json, queue, utils

# 配置 logging
logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.INFO)
logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.ERROR)

app = Flask(__name__)

dataQueue = queue.Queue()
producer = Producer(dataQueue)
consumer = Consumer(ThreadName = "consumerThread", DataQueue = dataQueue)
consumer.start()


# 检测请求接口
@app.route('/Detect', methods = ['POST'])
def Detect():
    try:
        requestData = request.json
        if 'imageData' not in requestData or not isinstance(requestData['imageData'], list):
            raise ValueError("The imageData parameter does not exist or is not an array")

        curTime = utils.GetTime()
        logging.info(f"[{curTime}]Successfully received the detection request")
        returnObj = {"Code": 200,
                     "msg": "OK",
                     "requestTime": curTime}
        producer.PutData(requestData)

    except Exception as e:
        curTime = utils.GetTime()
        requestData = request.json
        logging.error(f"[{curTime}]" + str(e))
        returnObj = {"Code": 400,
                     "msg": str(e)}

    finally:
        return jsonify(returnObj)


# 启动服务
def StartServer():
    try:
        app.run(host = "0.0.0.0", port = 8888, debug = False)
        curTime = utils.GetTime()
        logging.info(f"[{curTime}]Service started successfully")
    except Exception as e:
        logging.error(f"[{curTime}]" + str(e))


if __name__ == "__main__":
    StartServer()
