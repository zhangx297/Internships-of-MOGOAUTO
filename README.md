# 01/11/2023-01/02/2024 Internships：
1. Use of TAD (docker)
2. Linux development: tmux, Terminator, cosbrowser
3. Datasets processing
4. Model training
5. Quantification of Network Structure
6. Licence Plate Detection Models Training: YOLO V5n, YOLO V5s, YOLO V7-tiny
7. The Model Branch Training of Licence Recognition and Color Detection: CRNN
8. The Model Training of Body color: MobileNet, ResNet
9. Project: CMAKE，TensorRT
---------------------------------------------------------------------------
# Resignation Handover：
## 1. Licence Detection
```
Model Address: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main
```   
```
Datasets Address: /rss/zhangxutong/2023_Q4_detect_datasets
```
```
Logs of Model Address:
YOLOV5s-640: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov5s-640
YOLOV5s-320: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov5s-320
YOLOV5n-640: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov5-n-640
YOLOV5n-320: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov5-n-320
YOLOV7-tiny-640: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov7-tiny-640
YOLOV7-tiny-320: /rss/zhangxutong/Chinese_license_plate_detection_recognition-main/runs/train_yolov7-tiny-320
```
```
Datasets processing scripts: /rss/zhangxutong/2023_Q4_detect_datasets/small_size.py
```
## 2. Licence Recognition
```
Model Address: /rss/zhangxutong/crnn_plate_recognition-master
```
```
Datasets Address: /rss/zhangxutong/2023_Q4_recognition
```
```
Logs of Model Address: /rss/zhangxutong/crnn_plate_recognition-master/saved_model
```
```
Datasets processing scripts: /rss/zhangxutong/2023_Q4_recognition/recognition_datasets_processing.py
```
## 3. Licence Color Detection
```
Model Address: /rss/zhangxutong/crnn_plate_recognition-plate_color
```
```
Datasets Processing: /rss/zhangxutong/2023_Q4_color
```
```
Logs of Model Address: /rss/zhangxutong/crnn_plate_recognition-plate_color/saved_model
```
```
Datasets processing scripts: /rss/zhangxutong/2023_Q4_color/plate_datasets_processing.py
```
## 4. Project Address:
``` 
Model Address: /rss/zhangxutong/chinese_plate_tensorrt-master
```
```
Logs of Model Address: /rss/zhangxutong/chinese_plate_tensorrt-master/onnx_model
```
## 5. Body Color Detection
Model Address: /rss/zhangxutong/classification-pytorch-main
```
```
Datasets Address: /rss/zhangxutong/city_400_400
```
```
Logs of Model Address: /rss/zhangxutong/classification-pytorch-main/logs  
```
```
Licence Datasets Address of cosbrowser: algorithm-data-1255510688/RSS/city/2d/license_plate/
Original Licence json Datasets Address in TAD: /rss/zhangxutong/2023_Q4  
Original Licence txt Datasets Address in TAD: /rss/zhangxutong/2023_Q4_txt_jpg   
Original Body json Datasets Address in TAD: /rss/zhangxutong/city  
Original Body txt Datasets Address in TAD: /rss/zhangxutong/city_txt_jpg 
```
## 6. Training Process：
```
Datasets Processing：
    * Cosbrowser download to Server.
    * Convert format from json to txt label file.
    * Convert txt label file to datasets for licence detection, recognition, color detection. (The scripts is given at the above address)
```
```
Licence Detection：
    * Training Scripts：train.py
    * Inference Scripts：detect_plate.py
    * Transfer onnx scripts：export.py
```
```
Licence Recognition：
    * Training Scripts：train.py
    * Inference Scripts：demo.py
    * Transfer onnx scripts：export.py
    * Data Enhancement：demo1.py
```
```
Licence Color Detection：
    * Training Scripts：train_fix_color.py
    * Inference Scripts：demo_plate_color.py
    * Transfer onnx scripts：export.py
```
```
Body Color Detection：
    * Training Scripts：train.py
    * Inference Scripts：predict.py
```
