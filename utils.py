import tensorflow as tf
from tensorflow.keras.models import Model, load_model
import cv2
import numpy as np
import matplotlib.pyplot as plt

BRAIN_TUMOUR_MODEL = 'models/cnn-parameters-improvement-23-0.91.model'

class BrainTumourDiagnosisAgent:
    """
    This bot handles request for brain tumour detection based on MRI scans.

    Input:
        brain_image (numpy array)
    """
    def __init__(self, brain_image: np.array) -> None:

        self.model = load_model(filepath=BRAIN_TUMOUR_MODEL)

        # normalizing and rescaling the image to fit into the model
        self.image = cv2.resize(brain_image, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
        self.image = self.image/ 255.

    def diagnose(self) -> int:
        """
        :return: The probability from 0 to 100 of having a brain tumour
        """
        return round(self.model.predict(np.array([self.image]), verbose=0)[0][0]*100)