# import required module
import os
from ultralytics import YOLO
from PIL import Image
import cv2 as cv

model = YOLO("runs/detect/train3/weights/last.pt")
directory = 'example unknowns'

# iterate over files in
# that directory
# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     #run detection and save predictions
#     img = Image.open(filename)
#     results = model.predict(source=img, save=True)  # save plotted images
#     print(str(results.path))
filename = 'example unknowns/104712738-Accounting_101.jpg'

img = Image.open(filename)
results = model.predict(source=img, save=True)  # save plotted images
# print(results[0].boxes.)
DIR = os.path.join(results[0].save_dir,(os.listdir(results[0].save_dir))[0])
print(DIR)