import subprocess
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()
workFolder = os.getenv('ANN_FOR_DRONE_DATASET')
# Get the absolute path of the directory containing this script
base_dir=  os.path.abspath(os.path.dirname(workFolder))
# List of scripts to run
scripts = [
    os.path.join(base_dir,'txt_to_xml_Drone.py'),
    os.path.join(base_dir,'xml_to_json_Drone.py'),
    os.path.join(base_dir,'json_to_Txt_Drone.py'),
    os.path.join(base_dir,'text_to_json_Drone.py'),
]

for script in scripts:
    result = subprocess.run(['python', script], capture_output=True, text=True)
    print(f'Output of {script}:')
    print(result.stdout)
    print(result.stderr)
