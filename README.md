# Python Practical Programming Experiment Reports

This repository contains reports for two experiments conducted in the Python Practical Programming course.

## Experiment 1: Installing Python and PyCharm

This report details the process of setting up a Python programming environment. It covers the following topics:

- Installing Anaconda for Windows
- Installing PyCharm IDE
- Creating a new Python project in PyCharm
- Opening an existing Python project in PyCharm
- Packaging Python programs using conda

**Key Learnings:**

- Understanding the importance of setting up a dedicated Python environment using Anaconda.
- Familiarization with PyCharm IDE for streamlined code development.
- Introduction to basic Python concepts and problem-solving.

## Experiment 2: Installing Python Platforms and Object Detection with YOLOv8

This report explores the installation and utilization of various deep learning platforms, focusing on object detection using YOLOv8. It covers:

- Installing PyTorch for Windows
- Installing PaddlePaddle for Windows
- Installing TensorFlow for Windows
- Building and training a YOLOv8 object detection model with PyTorch
- Experimenting with different YOLO models and batch sizes

**Key Learnings:**

- Setting up popular deep learning frameworks (PyTorch, PaddlePaddle, TensorFlow) on Windows.
- Understanding the concept of object detection and its application with drone imagery.
- Building, training, and evaluating YOLOv8 models using the Ultralytics library.
- Exploring the impact of different model configurations and batch sizes on performance.

## Installation Instructions

To replicate the experiments, follow these installation steps:

1. **Install Anaconda:**

   - Download the Anaconda installer for Windows from the official website: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution).
   - Follow the installation instructions provided on the website.

2. **Create a Conda Environment:**

   - Open Anaconda Prompt.
   - Create a new environment named "CLASS_WORK":
     ```bash
     conda create -n CLASS_WORK
     ```
   - Activate the environment:
     ```bash
     conda activate CLASS_WORK
     ```

3. **Install PyCharm:**

   - Download the PyCharm Community Edition installer from: [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/).
   - Follow the installation instructions provided on the website.

4. **Install Required Libraries (within the "CLASS_WORK" environment):**

   - PyTorch:
     ```bash
     conda install pytorch torchvision torchaudio cpuonly -c pytorch
     ```
   - PaddlePaddle:
     ```bash
     conda install paddlepaddle==2.6.1 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
     ```
   - TensorFlow:
     ```bash
     pip install tensorflow
     ```
   - Ultralytics (for YOLOv8):
     ```bash
     pip install ultralytics
     ```

5. **Prepare Dataset:**
   - Organize your dataset of drone images and create a YAML file (e.g., `drone.yaml`) defining the dataset's structure and classes. Place this file within your project directory.

## Class 2: Object Detection with YOLO and Drone Data

**Objective:** Learn object detection using YOLO with drone data.

**Dataset:**

- Use the drone dataset located in the `DATASET` folder.

**Steps:**

1. **Load and Explore Data:**
   - Load the drone dataset into your chosen YOLO framework (e.g., Darknet, YOLOv5).
   - Explore the dataset structure, image formats, and annotations.
2. **Train a YOLO Model:**
   - Train a YOLO model using the drone dataset.
   - Experiment with different model configurations (e.g., YOLOv3, YOLOv5).
   - Adjust hyperparameters for optimal performance.
3. **Evaluate Model Performance:**
   - Evaluate the trained YOLO model on a separate validation set.
   - Analyze metrics like precision, recall, and mAP (mean Average Precision).

## Class 3: Neural Networks with PyTorch, PaddlePaddle, and TensorFlow

**Objective:** Learn about neural networks and their implementations using PyTorch, PaddlePaddle, and TensorFlow.

**Dataset:**

- Use the MNIST dataset of handwritten digits.

**Steps:**

1. **Introduction to Neural Networks:**
   - Learn the fundamental concepts of neural networks, including layers, activation functions, and backpropagation.
2. **Implement Neural Networks:**
   - Implement a simple neural network using PyTorch, PaddlePaddle, and TensorFlow.
   - Train and evaluate the network on the MNIST dataset.
   - Compare the performance and ease of use of the different frameworks.
3. **Explore Advanced Concepts:**
   - Explore more advanced concepts like convolutional neural networks (CNNs) and recurrent neural networks (RNNs).
   - Implement and train these advanced architectures on the MNIST dataset.

## Class 4: Building a Custom Annotated Dataset and Comparing Models

**Objective:** Create a custom annotated dataset and compare YOLO models trained on different datasets.

**Steps:**

1. **Create a New Conda Environment:**
   - Create a new conda environment named "labelimg" with Python 3.8:
     ```bash
     conda create --name labelimg python=3.8
     ```
2. **Activate the Environment:**
   - Activate the "labelimg" environment:
     ```bash
     conda activate labelimg
     ```
3. **Install labelImg:**
   - Install the labelImg tool:
     ```bash
     pip install labelImg
     ```
4. **Annotate Drone Images:**
   - Use labelImg to annotate your drone images.
   - Create a new folder for your self-annotated drone dataset (e.g., "SELF_ANNOTATED_DRONE_DATASET").
5. **Train YOLO Models with Different Datasets:**
   - Train two YOLO models:
     - **Model 1:** Trained on the original drone dataset (`DATASET_FOLDER`).
     - **Model 2:** Trained on the self-annotated dataset (`SELF_ANNOTATED_DRONE_DATASET`).
6. **Compare Model Performance:**
   - Evaluate both models and compare their performance.
   - Analyze the differences in performance based on the training data.
7. **Install dotenv:**
   - Install the dotenv library to manage environment variables:
     ```bash
     pip install dotenv
     ```
8. **Create .env File:**
   - Create a `.env` file and add the following lines:
     ```
     DATASET_FOLDER=your/dataset/path
     SELF_ANNOTATED_DRONE_DATASET=your/annotated/dataset/path
     ```
   - Replace `your/dataset/path` and `your/annotated/dataset/path` with the actual paths to your datasets.
9. **Update YAML Files:**
   - Update the paths in the relevant YAML files (`drone.yaml` or similar) to match the paths defined in your `.env` file.

## Class 5: Data Format Conversion and Script Automation

**Objective:** Learn how to convert annotation formats and automate script execution.

**Steps:**

1. **Convert Annotation Formats:**
   - Learn how to convert annotations between different formats (e.g., XML to TXT, JSON to XML).
   - Create scripts for each conversion type.
2. **Define Dataset Locations:**
   - Use environment variables in your `.env` file to define locations for your datasets:
     ```
     DATASET_FOLDER=your/dataset/path
     APPLE_DATASET=your/apple/dataset/path
     DRONE_DATASET=your/drone/dataset/path
     VOC_DATASET=your/voc/dataset/path
     ```
3. **Create New Folders for Annotated Data:**
   - Create new folders for each dataset, containing the annotations converted to the desired format.
   - Use Python scripts to process and convert annotations from the original format to the new format.
4. **Install subprocess:**
   - Install the `subprocess` library to execute scripts from your main script:
     ```bash
     pip install subprocess
     ```
5. **Create a Run All File:**
   - Create a new file (e.g., `run_all.py`) that uses `subprocess.run()` to execute all the conversion scripts for different datasets.
   - Define the paths to the scripts in your `.env` file:
     ```
     ANN_FOR_APPLE_DATASET=your/scripts/folder/path
     ANN_FOR_DRONE_DATASET=your/scripts/folder/path
     ```
   - Use `subprocess.run()` to execute the scripts in the specified folders.

**Note:** This is a comprehensive outline of the class content. You can adjust the specific topics and tasks based on your needs and the level of the students.

You are now ready to run the code examples and experiment with different configurations as described in the reports.
