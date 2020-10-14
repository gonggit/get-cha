from keras.models import load_model
from helpers import resize_to_fit
import numpy as np
import cv2
import pickle
import os


MODEL_FILENAME = "models/captcha_model.hdf5"
MODEL_LABELS_FILENAME = "models/model_labels.dat"


# Load up the model labels (so we can translate model predictions to actual letters)
with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)

# Load the trained neural network
model = load_model(MODEL_FILENAME)

def preprocess_image(image_file):
    filename = image_file.filename
    image_file.save(os.path.join('.', filename))

    path = os.getcwd()
    cmd = "convert %s/%s -negate -morphology erode octagon:1 -negate %s/transformed.png" % (path, filename, path)
    os.system(cmd)
    

def solve_captcha(image_file):
    preprocess_image(image_file)

    with open(MODEL_LABELS_FILENAME, "rb") as f:
        lb = pickle.load(f)

    model = load_model(MODEL_FILENAME)
    image = cv2.imread("transformed.png", cv2.IMREAD_GRAYSCALE)
    thresh = cv2.threshold(image, 200, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)[1]
    thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)

    letter_image_regions = []

    img_h, img_w = image.shape
    grid_w = 20 # crop width
    img_h = 40
    padding = 11

    for w in range(6):
        bbox = (padding + w * grid_w, 7, padding + (w + 1) * (grid_w), img_h - 2)
        letter_image_regions.append(bbox)

    if len(letter_image_regions) != 6:
        return ""

    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])
    predictions = []

    for letter_bounding_box in letter_image_regions:
        x, y, w, h = letter_bounding_box
        letter_image = thresh[y:h, x-1:w+1]
        letter_image = resize_to_fit(letter_image, 20, 20)
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        prediction = model.predict(letter_image)
        letter = lb.inverse_transform(prediction)[0]
        predictions.append(letter)

    return "".join(predictions)