from ultralytics import YOLO
from dotenv import load_dotenv
import os
# Load the environment variables from the .env file
load_dotenv()

model = YOLO('yolov8n.yaml').load('yolov8n.pt') # build from YAML and transfer weights
#DATASET_PATH
DATASET = os.getenv('DATASET_FOLDER')
PATH= os.path.join(DATASET+'drone.yaml')

# Train the model
results = model.train(data=PATH, epochs=10, imgsz=640 ,batch=2)

