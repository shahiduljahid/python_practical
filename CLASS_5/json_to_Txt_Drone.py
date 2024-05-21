import os
import json
from PIL import Image

# Define class names based on your YOLO classes
class_names = ["0"]  # You might have more classes
img_types = ['.JPEG', '.jpg']


def json_to_yolo(json_file, img_dir, output_dir):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the image filename from the JSON data
    base_filename = os.path.splitext(data['filename'])[0]
    img_file = next((os.path.join(img_dir, base_filename + ext) for ext in img_types if
                     os.path.isfile(os.path.join(img_dir, base_filename + ext))), None)

    if img_file is None:
        raise FileNotFoundError(f"No image file found for {base_filename} with supported types {img_types}")

    # Load the image to get its dimensions
    with Image.open(img_file) as img:
        img_width, img_height = img.size

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
        yolo_data.append(f"{class_id} {x_center} {y_center} {width} {height}")

    # Write to the YOLO format text file
    yolo_file = os.path.join(output_dir, base_filename + '.txt')
    with open(yolo_file, 'w') as f:
        f.write('\n'.join(yolo_data))


def convert_json_to_yolo(json_dir, img_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through JSON files in the directory
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            json_path = os.path.join(json_dir, json_file)
            json_to_yolo(json_path, img_dir, output_dir)


# ... (rest of your code)

folder_path='C:\\Users\\ADMIN\\Desktop\\Python_practical\\DATASET\\drone\\'
jsonToTxtTrainFolder = os.path.join(folder_path+'jsonToTextTrain')
jsonToTxtTestFolder = os.path.join(folder_path+'jsonToTextTest')

os.makedirs(jsonToTxtTrainFolder,exist_ok=True)
os.makedirs(jsonToTxtTestFolder,exist_ok=True)

jsonTrainFolder = os.path.join(folder_path+'XmlToJsonTrain')
jsonTestFolder = os.path.join(folder_path+'XmlToJsonTest')

trainFolder = os.path.join(folder_path+'train')
testFolder = os.path.join(folder_path+'test')

convert_json_to_yolo(jsonTrainFolder,trainFolder,jsonToTxtTrainFolder)
convert_json_to_yolo(jsonTestFolder,testFolder,jsonToTxtTestFolder)

# # Convert JSON to YOLO
# convert_json_to_yolo('./drone/txt2json_train', './drone/train', './drone/yolotrain')
# convert_json_to_yolo('./drone/txt2json_test', './drone/test', './drone/yolotest')
