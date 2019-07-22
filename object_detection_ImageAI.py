#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, redirect
import os, json
from imageai.Detection import ObjectDetection


# In[2]:


model_path = os.getcwd()


# In[3]:


PRE_TRAINED_MODELS =["yolo.h5"]


# In[4]:


# create imageAI objects and load models
object_detector =ObjectDetection()
object_detector.setModelTypeAsYOLOv3()
object_detector.setModelPath(os.path.join(model_path, PRE_TRAINED_MODELS[0]))
object_detector.loadModel()
object_detections = object_detector.detectObjectsFromImage(input_image="people_umbrella.jpg")


# In[5]:


#define model paths and allow file extention
UPLOAD_FOLDER =model_path
ALLOWED_EXTENSIONS =set(['png','jpg','jpeg','gif'])


# In[6]:


app =Flask(__name__)
app.config['UPLOAD_FOLDER'] =UPLOAD_FOLDER


# In[7]:


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


# In[8]:


@app.route('/predict',methods=['POST'])
def upload_file():
    if request.method =='POST':
        #check if the post request has the first part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file =request.files['file']
        # if user does not select file, brower also submit an empty part without filename
        if file.filename =='':
            print ('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename =file.filename
            file_path =os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(file_path)
        
        try:
            object_detections =object_detector.detectObjectsFromImage(input_image =file_path)
        except Exception as ex:
            return jsonify(str(ex))
        resp=[]
        for eachObject in object_detections:
            resp.append([eachObject["name"], round(eachObject["percentage_probability"],3)])
            
        return json.dumpa(dict(enumerate(resp)))


# In[ ]:


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=4445)

