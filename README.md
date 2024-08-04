# Survivor-detection-using-drone
Project Description:

The purpose of this project is to use drone technology for detecting survivors in disaster-affected areas. By employing a combination of computer vision techniques and machine learning algorithms, the drone can identify human presence in challenging environments, providing crucial information for rescue operations.

Table of Contents

- Introduction
- Features
- Installation
- Usage
- Project Structure
- Acknowledgements

Introduction

In disaster scenarios, timely detection and rescue of survivors can save lives. This project utilizes drone technology equipped with cameras and advanced algorithms to autonomously detect survivors from aerial footage. The system uses object detection models to identify human figures and provides their coordinates for rescue teams.

Features

- Autonomous drone navigation
- Real-time video feed analysis
- Human detection using machine learning models
- GPS coordinates of detected survivors
- User-friendly interface for monitoring and control

Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A drone with a camera (compatible with the project specifications)

Usage

1. Configure the Drone: Ensure the drone is set up and calibrated as per the manufacturer’s instructions.
2. Run the Detection Script: Execute the main detection script to start the drone and begin survivor detection.

Project Structure

```
Survivor-detection-using-drone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── object_detection_model.h5
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── detection.py
│
├── main.py
├── requirements.txt
└── README.md
```

- `data/`: Contains raw and processed data used for training and testing.
- `models/`: Pre-trained machine learning models for object detection.
- `scripts/`: Individual scripts for data preprocessing, model training, and detection logic.
- `main.py`: The main script to run the detection process.
- `requirements.txt`: List of dependencies required for the project.

Acknowledgements

- OpenCV
- TensorFlow
- DroneKitProject Description:

