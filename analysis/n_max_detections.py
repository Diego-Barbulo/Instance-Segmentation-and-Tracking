"""This module determines the maximum number of instances within one frame in order to fine-tune n_max_detections. 
This is necesarry to avoid AssertionErrors and limits RAM use. """

#Import libraries
import os
import numpy as np
import PIL.Image as Image
#Import modules
import config

def max_detections(train_dir, test_dir):
    sum=0
    dirs=[train_dir, test_dir]
    for folder in dirs:
        #Loop within train or testing folder
        path=os.path.join(folder, 'instances')
        #Loop through different datasets for training/testing
        for dataset in os.listdir(path):
            print(dataset)
            #Loop through all the instances of the datasets for training/testing
            for filename in os.listdir(os.path.join(path, dataset)):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    img = np.array(Image.open(os.path.join(os.path.join(path, dataset), filename)))
                    obj_ids = np.unique(img)
                    if len(obj_ids) > sum:
                        sum=len(obj_ids)
                else:
                    continue
    return sum

