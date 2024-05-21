import os
import json
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

def yolo_txt_to_json(txt_file, output_dir, class_names):
    """
    Converts a .txt annotation file in YOLO format to a JSON format.

    Args:
        txt_file (str): The path to the .txt annotation file.
        output_dir (str): The directory to save the JSON file.
        class_names (list): A list of class names corresponding to the class IDs in the .txt file.
    """

    try:
        # Read the .txt file
        with open(txt_file, 'r') as f:
            lines = f.readlines()

        # Extract filename from the path
        filename = os.path.splitext(os.path.basename(txt_file))[0]

        # Create the JSON data structure
        json_data = {
            "filename": filename,
            "objects": []
        }

        # Parse each line in the .txt file
        for line in lines:
            parts = line.strip().split(' ')
            class_id = int(parts[0])
            x_center = float(parts[1])
            y_center = float(parts[2])
            width = float(parts[3])
            height = float(parts[4])

            # Get the class name from the class_names list
            class_name = class_names[class_id]

            # Add the object data to the JSON
            json_data['objects'].append({
                "class_name": class_name,
                "x_center": x_center,
                "y_center": y_center,
                "width": width,
                "height": height
            })

        # Write the JSON data to a file
        json_file = os.path.join(output_dir, filename + '.json')
        with open(json_file, 'w') as f:
            json.dump(json_data, f, indent=4)

    except Exception as e:
        print(f"Error processing file {txt_file}: {e}")


def convert_yolo_txt_to_json(txt_dir, output_dir, class_names):
    """
    Converts all .txt annotation files in a directory to JSON format.

    Args:
        txt_dir (str): The directory containing the .txt files.
        output_dir (str): The directory to save the JSON files.
        class_names (list): A list of class names.
    """

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through .txt files in the directory
    for txt_file in os.listdir(txt_dir):
        if txt_file.endswith('.txt'):
            txt_path = os.path.join(txt_dir, txt_file)
            yolo_txt_to_json(txt_path, output_dir, class_names)

# Example usage:
DATASET = os.getenv('DRONE_DATASET')
folder_path= DATASET

txtToJSONTrainFolder = os.path.join(folder_path + 'txtToJSONTrain')
txtToJSONTestFolder = os.path.join(folder_path + 'txtToJSONTest')

os.makedirs(txtToJSONTrainFolder, exist_ok=True)
os.makedirs(txtToJSONTestFolder, exist_ok=True)

txtTrainFolder = os.path.join(folder_path + 'jsonToTextTrain')
txtTestFolder = os.path.join(folder_path + 'jsonToTextTest')

# Replace with your actual class names
class_names = ['drone']

convert_yolo_txt_to_json(txtTrainFolder, txtToJSONTrainFolder, class_names)
convert_yolo_txt_to_json(txtTestFolder, txtToJSONTestFolder, class_names)