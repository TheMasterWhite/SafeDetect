import logging
import sys

from flask import Flask, request, jsonify
from ultralytics import YOLO

if __name__ == '__main__':
    ModelList = {"exhaustFan": YOLO(model = "Weights/exhaustFan.pt", task = "detect"),
                 "gasTank": YOLO(model = "Weights/gasTank.pt", task = "detect"),
                 "gasTee": YOLO(model = "Weights/gasTee.pt", task = "detect"),
                 "regulator": YOLO(model = "Weights/regulator.pt", task = "detect")}
    result = ModelList["exhaustFan"](source = "https://masterwhite.oss-cn-guangzhou.aliyuncs.com/1657593135.jpg",
                                     save = True)
    print(result[0].tojson())
