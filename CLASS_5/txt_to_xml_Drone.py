import os
import xml.etree.ElementTree as ET


def yolo_to_xml(txt_file, output_dir, class_name):
    # Read the YOLO format text file
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    # Extract the image filename from the text file name
    filename = os.path.splitext(os.path.basename(txt_file))[0] + '.jpg'

    # Create the XML structure
    root = ET.Element('annotation')
    ET.SubElement(root, 'filename').text = filename

    size = ET.SubElement(root, 'size')
    ET.SubElement(size, 'width').text = str(img_width)
    ET.SubElement(size, 'height').text = str(img_height)
    ET.SubElement(size, 'depth').text = '3'

    # Iterate over each line in the text file
    for line in lines:
        parts = line.strip().split()
        class_name = parts[0]
        x_center, y_center, width, height = map(float, parts[1:])

        # Convert YOLO format coordinates back to XML format
        xmin = int((x_center - width / 2) * img_width)
        ymin = int((y_center - height / 2) * img_height)
        xmax = int((x_center + width / 2) * img_width)
        ymax = int((y_center + height / 2) * img_height)

        # Create object element
        obj = ET.SubElement(root, 'object')
        ET.SubElement(obj, 'name').text = class_name
        bndbox = ET.SubElement(obj, 'bndbox')
        ET.SubElement(bndbox, 'xmin').text = str(xmin)
        ET.SubElement(bndbox, 'ymin').text = str(ymin)
        ET.SubElement(bndbox, 'xmax').text = str(xmax)
        ET.SubElement(bndbox, 'ymax').text = str(ymax)

    # Write to the XML file
    xml_file = os.path.join(output_dir, os.path.splitext(os.path.basename(txt_file))[0] + '.xml')
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)


def convert_yolo_to_xml(txt_dir, output_dir, class_name):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through text files in the directory
    for txt_file in os.listdir(txt_dir):
        if txt_file.endswith('.txt'):
            txt_path = os.path.join(txt_dir, txt_file)
            yolo_to_xml(txt_path, output_dir, class_name)


# Define class names based on your YOLO classes
class_name = ["drone"]

# Assuming img_width and img_height are known (you can set these values accordingly)
img_width = 640  # Example value, replace with actual width
img_height = 480  # Example value, replace with actual height

folder_path='C:\\Users\\ADMIN\\Desktop\\Python_practical\\CLASS_5\\drone\\'
textToXmlTrainFolder = os.path.join(folder_path+'textToXmlTrain')
txtToXmlTestFolder = os.path.join(folder_path+'textToXmlTest')

os.makedirs(textToXmlTrainFolder,exist_ok=True)
os.makedirs(txtToXmlTestFolder,exist_ok=True)

txtTrainFolder = os.path.join(folder_path+'train')
txtTestFolder = os.path.join(folder_path+'test')

# Convert YOLO to XML
convert_yolo_to_xml(txtTrainFolder,textToXmlTrainFolder,class_name)
convert_yolo_to_xml(txtTestFolder,txtToXmlTestFolder,class_name)
