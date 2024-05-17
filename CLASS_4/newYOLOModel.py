from ultralytics import YOLO

model1 = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
PATH1 = r'C:\Users\ADMIN\Desktop\Python_practical\pythonpa\dataset\drone.yaml'
# Train the model
results = model1.train(data=PATH1, epochs=20, imgsz=1000 ,batch=2)

model2 = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
PATH2 = r'C:\Users\ADMIN\Desktop\Python_practical\CLASS_4\drone.yaml'
# Train the model
results = model2.train(data=PATH2, epochs=20, imgsz=1000 ,batch=2)