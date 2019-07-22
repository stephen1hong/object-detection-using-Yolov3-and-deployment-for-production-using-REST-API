# object-detection-using-pretrained-deep-learning-Yolov3
Reference: python deep learning projects, M. Lamons, R. Kumar, A. Nagaraja

* Step 1: load pre-trained deep learning model such as Yolov3, resnet, etc.

* Step 2: feed new images to the model for detection. 
  *  The result return the image with bounding box coordinates of the detected object, the label of the detected object and the confidence score for the detected object.
  
 # deploying the model for production using REST API
 * Step 3: under Terminal run such command:
     * object_detection_ImageAI.py
 * step 4: call the API in a separate Terminal by the folowing command (e.g.,):
    * curl -X POST http://0.0.0.0:4445/predict -H 'content-type: multipart/form-data;boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' -F file=@/Users/Owner/Downloads/person_hourse_dog.jpg
