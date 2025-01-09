
import cv2

def detect_objects(image_path, model_path, config_path, classes_path):
    # Load YOLO model
    net = cv2.dnn.readNet(model_path, config_path)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    # Load class names
    with open(classes_path, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    # Load image
    image = cv2.imread(image_path)
    height, width, channels = image.shape

    # Create blob and detect objects
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    detections = net.forward(output_layers)

    # Process detections
    for detection in detections:
        for object_detected in detection:
            scores = object_detected[5:]
            class_id = scores.argmax()
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(object_detected[0] * width)
                center_y = int(object_detected[1] * height)
                print(f"Detected {classes[class_id]} with confidence {confidence:.2f} at ({center_x}, {center_y})")

if __name__ == "__main__":
    detect_objects("sample.jpg", "yolov3.weights", "yolov3.cfg", "coco.names")
