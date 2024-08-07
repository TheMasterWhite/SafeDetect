from ultralytics import YOLO
import json

# ����ģ��
ModelList = {"exhaustFan": YOLO(model = "Weights/exhaustFan.pt", task = "detect"),
             "gasTank": YOLO(model = "Weights/gasTank.pt", task = "detect"),
             "gasTee": YOLO(model = "Weights/gasTee.pt", task = "detect"),
             "regulator": YOLO(model = "Weights/regulator.pt", task = "detect")}


# YOLO���ӿ�
def Detect(ImageUrl):
    try:
        resultList = []
        for model in ModelList.values():
            tmpResult = model(source = ImageUrl)
            resultList.append(tmpResult[0].tojson())

        return resultList

    except Exception as e:
        raise e
