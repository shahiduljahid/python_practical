from ultralytics import YOLO

model1 = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
PATH1 = '/Users/macbook/Desktop/python_practical/pythonpa/dataset/drone.yaml'
# Train the model
results = model1.train(data=PATH1, epochs=10, imgsz=640 ,batch=1)

model2 = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
PATH2 = '/Users/macbook/Desktop/python_practical/CLASS_4/drone.yaml'
# Train the model
results = model2.train(data=PATH2, epochs=10, imgsz=640 ,batch=1)