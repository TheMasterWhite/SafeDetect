from ultralytics import YOLO
import json

# Load a pretrained YOLOv8n model
#model = YOLO("yamls/Gas tank.yaml",task = "detect")
model = YOLO("weights/Gas tank煤气罐/best.pt",
             task = "detect")

# Define path to the image file
source = "data/1657593135.jpg"

# Run inference on the source
# results = model(source)  # list of Results objects
results = model.predict(source = source)
a = results[0]
b = a.tojson()
print(b)

