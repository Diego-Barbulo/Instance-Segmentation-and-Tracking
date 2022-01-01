"""This module gives an overview of both the test and train dataset. It will output the name, resolution, number
of frames, tracks and masks"""

#Import libraries
import numpy as np
import PIL.Image as Image
import os
import math
import pandas as pd
#Import modules
import config

def overview(train_dir, test_dir):
    dirs=[train_dir, test_dir]
    dicts={}
    for folder in dirs:
        #Loop within train or testing folder
        path=os.path.join(folder, 'instances')
        #Loop through different datasets for training/testing
        for dataset in os.listdir(path):
            print(dataset)
            mask=0
            track=0
            frames=0
            #Loop through all the instances of the datasets for training/testing
            for filename in os.listdir(os.path.join(path, dataset)):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    frames+=1
                    img = np.array(Image.open(os.path.join(os.path.join(path, dataset), filename)))
                    obj_ids = np.unique(img)
                    mask+=int(len(obj_ids)-1)
                    if np.max(obj_ids) > track:
                        track = np.max(obj_ids)
                else:
                    continue
            track_id = track % 1000
            ls=[frames,track_id, mask]
            dicts[dataset]=ls
    df=pd.DataFrame.from_dict(dicts,orient='index', columns=['#frames', '#tracks', ' #masks'])
    return df