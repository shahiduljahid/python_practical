from ultralytics import YOLO

model = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
PATH = 'C:\\Users\\ADMIN\\Desktop\\Python_practical\\pythonpa\\dataset\\drone.yaml'
# Train the model
results = model.train(data=PATH, epochs=10, imgsz=640 ,batch=2)

