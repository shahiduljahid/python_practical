#JSON TO TXT
import os
import json
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()
# Define class names based on your YOLO classes
class_names = ["apple", "banana","orange"]  # Add "banana" if it's a valid class  # You might have more classes
img_types = ['.JPEG', '.jpg']


def json_to_yolo(json_file, output_dir):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the image filename from the JSON data
    base_filename = os.path.splitext(data['filename'])[0]

    # Prepare the YOLO format data
    yolo_data = []

    # Iterate over each object in the JSON file
    for obj in data['objects']:
        class_id = class_names.index(obj['class_name'])  # Get class ID

        # Calculate YOLO coordinates (already normalized)
        x_center = obj['x_center']
        y_center = obj['y_center']
        width = obj['width']
        height = obj['height']

        # Append to YOLO data list
        yolo_data.append(f"{class_names[class_id]} {x_center} {y_center} {width} {height}")

    # Write to the YOLO format text file
    yolo_file = os.path.join(output_dir, base_filename + '.txt')
    with open(yolo_file, 'w') as f:
        f.write('\n'.join(yolo_data))


def convert_json_to_yolo(json_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through JSON files in the directory
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_dir, json_file)
            json_to_yolo(json_path, output_dir)

# ... (rest of your code)

DATASET = os.getenv('APPLE_DATASET')
folder_path= DATASET
jsonToTxtTrainFolder = os.path.join(folder_path + 'jsonToTextTrain')
jsonToTxtTestFolder = os.path.join(folder_path + 'jsonToTextTest')

os.makedirs(jsonToTxtTrainFolder, exist_ok=True)
os.makedirs(jsonToTxtTestFolder, exist_ok=True)

jsonTrainFolder = os.path.join(folder_path + 'XmlToJsonTrain')
jsonTestFolder = os.path.join(folder_path + 'XmlToJsonTest')

convert_json_to_yolo(jsonTrainFolder, jsonToTxtTrainFolder)  # No image directory needed
convert_json_to_yolo(jsonTestFolder, jsonToTxtTestFolder)  # No image directory needed