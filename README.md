## Python Practical Programming Experiment Reports 📚🚀

This repository contains reports for two experiments conducted in the Python Practical Programming course.

### Initial Setup 🛠️

**Create .env File:**

- Create a `.env` file and store your dataset paths like this:
  **Install dotenv:**
- Install the dotenv library to manage environment variables:

```bash
pip install dotenv
```

```
DATASET_FOLDER=
APPLE_DATASET=
APPLE_DATASET_WITH_IMG=
DRONE_DATASET=
VOC_DATASET=
ANN_FOR_APPLE_DATASET=
ANN_FOR_DRONE_DATASET=
SELF_ANNOTATED_DRONE_DATASET=
MODEL_FOLDER_PATH=
```

### Dataset & Models:

- [DOWNLOAD DATASETS AND MODELS ](https://github.com/shahiduljahid/DATASET_AND_MODELS)
- Use these models to test your code and explore their parameters.

### Experiment 1: Installing Python and PyCharm 🐍💻

**Install PyCharm:**

- Download the PyCharm Community Edition installer from [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/).
- Follow the installation instructions on the website.

### Experiment 2: Installing Python Platforms and Object Detection with YOLOv8 🧠🤖

This report delves into installing and using various deep learning platforms, focusing on object detection using YOLOv8. We'll cover:

- Installing PyTorch for Windows
- Installing PaddlePaddle for Windows
- Installing TensorFlow for Windows
- Building and training a YOLOv8 object detection model with PyTorch
- Experimenting with different YOLO models and batch sizes

**Key Learnings:**

- Setting up popular deep learning frameworks (PyTorch, PaddlePaddle, TensorFlow) on Windows.
- Understanding the concept of object detection and its application with drone imagery 🚁
- Building, training, and evaluating YOLOv8 models using the Ultralytics library
- Exploring the impact of different model configurations and batch sizes on performance 📈

### Installation Instructions 🛠️

To replicate the experiments, follow these installation steps:

1. **Install Anaconda:**
   - Download the Anaconda installer for Windows from [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution).
   - Follow the installation instructions on the website.
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
3. **Install Required Libraries (within the "CLASS_WORK" environment):**
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
4. **Prepare Dataset:**
   - Organize your dataset of drone images and create a YAML file (e.g., `drone.yaml`) defining the dataset's structure and classes. Place this file within your project directory.

### Class 2: Object Detection with YOLO and Drone Data 🚁

**Objective:** Learn object detection using YOLO with drone data.

**Dataset:**

- Use the drone dataset located in the `DATASET` folder.

**Steps:**

1. **Load and Explore Data:**
   - Load the drone dataset into your chosen YOLO framework (e.g. YOLOv8).
   - Explore the dataset structure, image formats, and annotations.
2. **Train a YOLO Model:**
   - Train a YOLO model using the drone dataset.
3. **Evaluate Model Performance:**
   - Evaluate the trained YOLO model on a separate validation set.
   - Analyze metrics like precision, recall, and mAP (mean Average Precision).

### Class 3: Neural Networks with PyTorch, PaddlePaddle, and TensorFlow 🧠

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

### Class 4: Building a Custom Annotated Dataset and Comparing Models 🛠️

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
7. **Create Folder Path in .env File:**

   ```
   DATASET_FOLDER=your/dataset/path
   SELF_ANNOTATED_DRONE_DATASET=your/annotated/dataset/path
   ```

   - Replace `your/dataset/path` and `your/annotated/dataset/path` with the actual paths to your datasets.

8. **Update YAML Files:**
   - Update the paths in the relevant YAML files (`drone.yaml` or similar) to match the paths defined in your `.env` file.

### Class 5: Data Format Conversion and Script Automation 🤖

**Objective:** Learn how to convert annotation formats and automate script execution.

**Steps:**

1. **Convert Annotation Formats:**
   - Learn how to convert annotations between different formats (e.g., XML to TXT, JSON to XML).
   - Create scripts for each conversion type.
2. **Define Dataset Locations:**
   -define locations for your datasets:
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
   - To run all the script at a time files like (e.g., run_all_APPLE_DATASET ) .
   - Define the paths to the scripts in your `.env` file:
     ```
     ANN_FOR_APPLE_DATASET=your/scripts/folder/path
     ANN_FOR_DRONE_DATASET=your/scripts/folder/path
     ```

## Class 6: Convolutional Neural Networks (CNNs) and YOLOv1 🍎🧠

**Objective:** Learn about Convolutional Neural Networks (CNNs) and implement a YOLOv1 model for fruit detection.

**Dataset:**

- Use the `Apple Dataset with Images` (`./appledataset_with_img/`) located in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS).

**Model:**

- **Download:** A trained YOLOv1 model for this dataset is available in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS) as "Model 1".
- **Train your own:** You can also train your own model. Follow the steps below:

**Setup:**

1. **Install `scikit-image`:**
   ```bash
   pip install scikit-image
   ```

## Set Environment Variables:

In your `.env` file, ensure these keys are defined:

- **`APPLE_DATASET_WITH_IMG`**: Set to the path of the `Apple Dataset with Images` (`./appledataset_with_img/`).
- **`MODEL_FOLDER_PATH`**: Set to the path where you want to save your trained model (or where you downloaded the trained model).

## Choose Device:

The code is set up for CPU (`DEVICE = "cpu"`). If you have a CUDA-enabled GPU, change it to `DEVICE = "cuda"`.

## Training:

### Training Section:

The code will have a section marked as:

```
#MODEL TRAINING AND SAVING PART START
.
.
code
.
.
#MODEL TRAINING AND SAVING PART FINISH
```

### Comment Training Code:

To use the trained model, comment out the code between the "MODEL TRAINING AND SAVING PART START" and "MODEL TRAINING AND SAVING PART FINISH" markers.

## Running the Code:

Running the code will generate output files in an "output" folder.

## Class 7: Fast R-CNN for Fruit Detection 🍎🧠

**Objective:** Learn about Fast R-CNN and implement it for fruit detection.

**Dataset:**

- Same as Class 6: Use the `Apple Dataset with Images` located in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS).

**Model:**

- **Download:** A trained Fast R-CNN model for this dataset is available in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS) as "Model 2".
- **Train your own:** You can also train your own model.

**Setup:**

- No additional setup required if you've completed Class 6. The environment variables and installation steps are the same.

**Training:**

- Similar to Class 6, you can train a Fast R-CNN model from scratch.
- Use the same commenting approach to skip training and use the trained model.

**Running the Code:**

- Running the code will generate output files in an "output" folder.

**Key Points:**

- **Environment Variables:** Carefully set the necessary environment variables in your `.env` file.
- **trained Models:** Make sure the `MODEL_FOLDER_PATH` points to the correct location of your downloaded model if you want to use a trained model.

## Class 8: Jupyter for IMAGE SEGMENTATION

**Objective:** 🧑‍🏫 Learn about Jupyter and SEGMENTATION

**Dataset:**

- Use the `FOOTBALL Dataset` located in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS).
- Use the `CITYSCAPE Dataset` located in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS).

### **Model 3: Football model with FOOTBALL Dataset** ⚽

- **Download:** A trained football model for this dataset is available in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS) as `Model 3`.
- **Train your own:** You can also train your own model.

**Setup:**

### Set Environment Variables:

In your `.env` file, ensure these keys are defined:

- **`FOOTBALL_DATASET`**: Set to the path of the `FOOTBALL_DATASET`.
- **`MODEL_FOLDER_PATH`**: Set to the path where you want to save your trained model (or where you downloaded the trained model).

### Choose Device:

The code is set up for CPU (`DEVICE = "cpu"`). If you have a CUDA-enabled GPU, change it to `DEVICE = "cuda"`.

### Training:

#### Training Section:

The code will have a section marked as:

```
#MODEL TRAINING AND SAVING PART START
.
.
code
.
.
#MODEL TRAINING AND SAVING PART FINISH
```

```
#MODEL TRAINING PLOT START
.
.
code
.
.
#MODEL TRAINING PLOT FINISH
```

#### Comment Training AND PLOT Code:

To use the trained model, comment out the code between the `MODEL TRAINING AND SAVING PART START` and `MODEL TRAINING AND SAVING PART FINISH` markers. Also comment out the code between the `MODEL TRAINING PLOT START` and `MODEL TRAINING PLOT FINISH` markers.

### Running the Code:

Running the code will generate output files in an `output/football` folder.

### **Model 4: Unet1 model with CITYSCAPE Dataset** 🌆

- **Download:** A trained Unet1 model trained on cityscape data is available in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS) as `Model 4`.
- **Train your own:** You can also train your own model.

**Setup:**

### Set Environment Variables:

In your `.env` file, ensure these keys are defined:

- **`CITY_SCAPES_DATASET`**: Set to the path of the `CITY_SCAPES_DATASET`.
- **`MODEL_FOLDER_PATH`**: Set to the path where you want to save your trained model (or where you downloaded the trained model).

### Choose Device:

The code is set up for CPU (`DEVICE = "cpu"`). If you have a CUDA-enabled GPU, change it to `DEVICE = "cuda"`.

### Training:

#### Training Section:

The code will have a section marked as:

```
#MODEL TRAINING AND SAVING PART START
.
.
code
.
.
#MODEL TRAINING AND SAVING PART FINISH
```

```
#MODEL TRAINING PLOT START
.
.
code
.
.
#MODEL TRAINING PLOT FINISH
```

#### Comment Training AND PLOT Code:

To use the trained model, comment out the code between the `MODEL TRAINING AND SAVING PART START` and `MODEL TRAINING AND SAVING PART FINISH` markers. Also comment out the code between the `MODEL TRAINING PLOT START` and `MODEL TRAINING PLOT FINISH` markers.

### Running the Code:

Running the code will generate output files in an `output/city_unet1` folder.

### **Model 5: 6 Different models with CITYSCAPE Dataset** 🌆

- **Download:** `6 model` trained on cityscape data is available in the [dataset repository](https://github.com/shahiduljahid/DATASET_AND_MODELS) as `Model 5`.
- **Train your own:** You can also train your own model.

**Setup:**

### Set Environment Variables:

In your `.env` file, ensure these keys are defined:

- **`CITY_SCAPES_DATASET`**: Set to the path of the `CITY_SCAPES_DATASET`.
- **`MODEL_FOLDER_PATH`**: Set to the path where you want to save your trained model (or where you downloaded the trained model).

### Choose Device:

The code is set up for CPU (`DEVICE = "cpu"`). If you have a CUDA-enabled GPU, change it to `DEVICE = "cuda"`.

### Training:

#### Training Section:

The code will have a section marked as:

```
#MODEL TRAINING AND SAVING PART START
.
.
code
.
.
#MODEL TRAINING AND SAVING PART FINISH
```

```
#MODEL TRAINING PLOT START
.
.
code
.
.
#MODEL TRAINING PLOT FINISH
```

#### Comment Training AND PLOT Code:

To use the trained model, comment out the code between the `MODEL TRAINING AND SAVING PART START` and `MODEL TRAINING AND SAVING PART FINISH` markers. Also comment out the code between the `MODEL TRAINING PLOT START` and `MODEL TRAINING PLOT FINISH` markers.

### Running the Code:

Running the code will generate output files in an `output/city6_models` folder.

**Note:** This is a comprehensive outline of the class content. You can adjust the specific topics and tasks based on your needs and the level of the students.

You are now ready to run the code examples and experiment with different configurations as described in the reports.
