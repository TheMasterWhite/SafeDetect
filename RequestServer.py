import logging

import requests, json
import utils

data2 = {"data": 123}


# 发送结果请求
def PushResult(Result, Type, ImgId):
    try:
        url = "http://222.240.1.44:38080/addInfer"
        data = {"oper": Type,
                "imgId": ImgId,
                "safeType": "0",
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
            logging.info(f"[{curTime}]结果发送成功")
        else:
            logging.info(f"[{curTime}]结果发送失败")

    except Exception as e:
        raise e


if __name__ == "__main__":
    list = [
        {
            "name": "Gas tank",
            "class": 0,
            "confidence": 0.97412,
            "box": {
                "x1": 46.93078,
                "y1": 35.63008,
                "x2": 455.09277,
                "y2": 866.84601
            }
        }
    ]
    PushResult(list, "gasTank", 0)
