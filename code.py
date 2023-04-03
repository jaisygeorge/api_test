import numpy as np
import pandas as pd
import pickle

import warnings
warnings.filterwarnings("ignore")
#import tensorflow
import keras

from keras.models import load_model

# load pre-trained model
#model = load_model('model_Mar29_2')

# load the scaler and pca objects from disk
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('pca.pkl', 'rb') as f:
    pca = pickle.load(f)
    
print("Hello World")
    
