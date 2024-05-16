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

You are now ready to run the code examples and experiment with different configurations as described in the reports.
