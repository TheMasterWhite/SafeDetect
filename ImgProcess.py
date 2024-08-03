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
        saveImage = data.get("saveImage", False)
        saveTxt = data.get("saveText", False)
        model = ModelList[type]
        resultList = model(source = imageUrl,
                           save = saveImage,
                           save_txt = saveTxt,
                           save_conf = saveTxt)
        result = resultList[0]
        saveDir = result.save_dir

        if saveImage or saveTxt:
            # do something here
            pass

        return result.tojson()

    except Exception as e:
        raise e
