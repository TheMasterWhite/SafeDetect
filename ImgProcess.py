from ultralytics import YOLO
import json, logging

# 加载模型
ModelList = {"exhaustFan": YOLO(model = "Weights/exhaustFan.pt", task = "detect"),
             "gasTank": YOLO(model = "Weights/gasTank.pt", task = "detect"),
             "gasTee": YOLO(model = "Weights/gasTee.pt", task = "detect"),
             "regulator": YOLO(model = "Weights/regulator.pt", task = "detect")}


# YOLO检测接口
def Detect(ImageUrl):
    try:
        resultList = []
        for model in ModelList.values():
            tmpResult = model(source = ImageUrl)
            detectResult = tmpResult[0].tojson()
            resultList.append(json.loads(detectResult))
        return resultList

    except Exception as e:
        raise e
