import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

VOC_CLASSES = (    # always index 0
    'aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')

def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    if xml_file.endswith('.xml'):
        tree = ET.parse(filename)
        objects = []
        for obj in tree.findall('object'):
            obj_struct = {}
            difficult = int(obj.find('difficult').text)
            if difficult == 1:
                continue
            obj_struct['name'] = obj.find('name').text
            bbox = obj.find('bndbox')
            obj_struct['bbox'] = [int(float(bbox.find('xmin').text)),
                                int(float(bbox.find('ymin').text)),
                                int(float(bbox.find('xmax').text)),
                                int(float(bbox.find('ymax').text))]
            objects.append(obj_struct)

        return objects
    
DATASET = os.getenv('VOC_DATASET')
folder_path= DATASET

txt_file_path =  os.path.join(folder_path+'voc2007test.txt')
print(txt_file_path)
txt_file = open(txt_file_path,'w')

Annotations_folder_path = os.path.join(folder_path+'Annotations')
xml_files = os.listdir(Annotations_folder_path)

count = 0
for xml_file in xml_files:
    count += 1
    image_path = xml_file.split('.')[0] + '.jpg'
    results = parse_rec(os.path.join(Annotations_folder_path, xml_file))
    if len(results)==0:
        print(xml_file)
        continue
    txt_file.write(image_path)
    for result in results:
        class_name = result['name']
        bbox = result['bbox']
        class_name = VOC_CLASSES.index(class_name)
        txt_file.write(' '+str(bbox[0])+' '+str(bbox[1])+' '+str(bbox[2])+' '+str(bbox[3])+' '+str(class_name))
    txt_file.write('\n')
txt_file.close()