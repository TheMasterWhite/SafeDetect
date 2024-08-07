from ultralytics import YOLO
import json

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
            resultList.append(tmpResult[0].tojson())

        return resultList

    except Exception as e:
        raise e
