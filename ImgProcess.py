from ultralytics import YOLO

# ����ģ��
ModelList = {"exhaustFan": YOLO(model = "Weights/exhaustFan.pt", task = "detect"),
             "gasTank": YOLO(model = "Weights/gasTank.pt", task = "detect"),
             "gasTee": YOLO(model = "Weights/gasTee.pt", task = "detect"),
             "regulator": YOLO(model = "Weights/regulator.pt", task = "detect")}


# YOLO���ӿ�
def Detect(data):
    try:
        imageUrl = data.get("imageUrl")
        type = data.get("type")
        model = ModelList[type]
        resultList = model(source = imageUrl,
                           save = True)
        result = []
        for i in resultList:
            result += i.tojson()

        return result

    except Exception as e:
        raise e
