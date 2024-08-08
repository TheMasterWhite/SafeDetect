import logging

import requests, json
import utils

logging.basicConfig(filename = "Logs/server.log",
                    filemode = 'a',
                    level = logging.INFO)


# 发送结果请求
def PushResult(Result, Type, ImgId, SafeType):
    try:
        url = "http://222.240.1.44:38080/addInfer"
        data = {"oper": Type,
                "imgId": ImgId,
                "safeType": SafeType,
                "indexUrl": "NULL"}
        headers = {'Content-Type': 'application/json'}
        resultContent = ""
        # 遍历所有结果框获取数据
        for img in Result:
            box = img["box"]
            resultContent += str(box["x1"]) + " " + str(box["y1"]) + " " + str(box["x2"]) + " " + str(box["y2"]) + "\n"
        data["indexUrl"] = resultContent
        response = requests.post(url, data = json.dumps(data), headers = headers)
        message = json.loads(response.text)

        # 记录日志
        curTime = utils.GetTime()
        status = message["msg"]
        if status == "success":
            logging.info(f"[{curTime}]Results sent successfully")
        else:
            logging.info(f"[{curTime}]Results sent failed")

    except Exception as e:
        curTime = utils.GetTime()
        logging.error(f"[{curTime}]{str(e)}")


def PushNullResult(Type, ImgId, SafeType):
    try:
        url = "http://222.240.1.44:38080/addInfer"
        data = {"oper": Type,
                "imgId": ImgId,
                "safeType": SafeType,
                "indexUrl": "NULL"}
        headers = {'Content-Type': "application/json"}
        response = requests.post(url, data = json.dumps(data), headers = headers)
        message = json.loads(response.text)

        # 记录日志
        curTime = utils.GetTime()
        status = message["msg"]
        if status == "success":
            logging.info(f"[{curTime}]Null results sent successfully")
        else:
            logging.info(f"[{curTime}]Null results sent failed")

    except Exception as e:
        curTime = utils.GetTime()
        logging.error(f"[{curTime}]{str(e)}")
