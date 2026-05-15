
# Drone Human Detection & Counting System

## Overview
This project was developed for the Antlings AI/ML Technical Assessment.

The system detects:
- Humans
- Cars

from drone/aerial imagery using YOLOv8.

It also:
- counts total humans
- visualizes detections
- displays confidence scores
- saves processed outputs

---

## Model Used
- YOLOv8 Nano (YOLOv8n)

---

## Dataset
VisDrone Dataset:
https://www.kaggle.com/datasets/banuprasadb/visdrone-dataset

---

## Features
✅ Human Detection
✅ Car Detection
✅ Human Counting
✅ Bounding Box Visualization
✅ Confidence Score Display
✅ Processed Output Saving

---

## Training Details

- Epochs: 20
- Image Size: 640
- Batch Size: 16
- GPU: Tesla T4

---

## Results

### Validation Metrics
- mAP50: ~0.51
- Human Detection mAP50: ~0.30
- Car Detection mAP50: ~0.71

---

## Challenges Faced

- Small object detection
- Dense crowd regions
- Occlusion
- Scale variation
- Drone viewpoint complexity

---

## Run Inference

python detect_count.py \
    --model weights/best.pt \
    --image sample.jpg \
    --output result.jpg

---

## Project Structure

Antlings_Drone_Detection_Project/
│
├── detect_count.py
├── README.md
├── weights/
├── results/
├── sample_outputs/

---

## Author
AI/ML Internship Assessment Submission
