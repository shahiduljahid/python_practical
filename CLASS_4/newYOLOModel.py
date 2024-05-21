from ultralytics import YOLO
from dotenv import load_dotenv
import os
# Load the environment variables from the .env file
load_dotenv()

 # build from YAML and transfer weights
model = YOLO('yolov8n.yaml').load('yolov8n.pt')

#DATASET_PATH
DATASET = os.getenv('DATASET_FOLDER')

#FIRST_DATASET TRAIN
PATH1= os.path.join(DATASET+'drone.yaml')
# Train the model
results = model.train(data=PATH1, epochs=1, imgsz=1000 ,batch=2)

#SELF_ANNOTATED_DATASET TRAIN
NEW_ANNOTATED_DATASET = os.getenv('SELF_ANNOTATED_DRONE_DATASET')
PATH2= os.path.join(NEW_ANNOTATED_DATASET+'drone.yaml')
# # Train the model
results = model.train(data=PATH2, epochs=1, imgsz=1000 ,batch=2)
