#XML TO TXT

import os
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

def xml_to_yolo(xml_file, output_dir):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract relevant information
    filename = root.find('filename').text
    img_width = int(root.find('size').find('width').text)
    img_height = int(root.find('size').find('height').text)

    # Open the text file for writing
    txt_file = os.path.join(output_dir, os.path.splitext(filename)[0] + '.txt')
    with open(txt_file, 'w') as f:
        # Iterate over each object in the XML file
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)

            # Calculate YOLO format coordinates
            x_center = (xmin + xmax) / (2 * img_width)
            y_center = (ymin + ymax) / (2 * img_height)
            width = (xmax - xmin) / img_width
            height = (ymax - ymin) / img_height

            # Write to the text file in YOLO format
            f.write(f"{class_name} {x_center} {y_center} {width} {height}\n")

def convert_xml_to_yolo(xml_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through XML files in the directory
    for xml_file in os.listdir(xml_dir):   
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_file)
            xml_to_yolo(xml_path, output_dir)

DATASET = os.getenv('APPLE_DATASET')
folder_path= DATASET

xmlToTxtTrainFolder = os.path.join(folder_path+'xmlToTxtTrain')
xmlToTxtTestFolder = os.path.join(folder_path+'xmlToTxtTest')

os.makedirs(xmlToTxtTrainFolder,exist_ok=True)
os.makedirs(xmlToTxtTestFolder,exist_ok=True)

xmlTrainFolder = os.path.join(folder_path+'train')
xmlTestFolder = os.path.join(folder_path+'test')

convert_xml_to_yolo(xmlTrainFolder ,xmlToTxtTrainFolder)
convert_xml_to_yolo(xmlTestFolder ,xmlToTxtTestFolder)
