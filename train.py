from ultralytics import YOLO
import torch
# print(torch.cuda.device_count())
# # SETUP GPU
# device = "0" if torch.cuda.is_available() else "cpu"
#
# if device == "0":
#     torch.cuda.set_device(0)
# # Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')
# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='config.yaml', epochs=15)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
# results = model('https://ultralytics.com/images/bus.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')