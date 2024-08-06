from ultralytics import YOLO
import json

# 加载模型
ModelList = {"exhaustFan": YOLO(model = "Weights/exhaustFan.pt", task = "detect"),
             "gasTank": YOLO(model = "Weights/gasTank.pt", task = "detect"),
             "gasTee": YOLO(model = "Weights/gasTee.pt", task = "detect"),
             "regulator": YOLO(model = "Weights/regulator.pt", task = "detect")}


# YOLO检测接口
def Detect(ImageUrl, Type):
    try:
        model = ModelList[Type]
        resultList = model(source = ImageUrl)
        result = resultList[0]
        return json.loads(result.tojson())

    except Exception as e:
        raise e
