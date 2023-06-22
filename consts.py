import cv2


MODEL_PATH = 'best.pt'
PYTESSARACT_PATH = r'C:\Users\irfan baykara\Desktop\TrafficSignsDetectorYolov8\tessdata'
TESSDATA_CONFIG = r'C:\\Users\\irfan baykara\\Desktop\TrafficSignsDetectorYolov8\\tessdata'
FONT = cv2.FONT_HERSHEY_SIMPLEX
BLUE_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
CLASSES = ['stop', 'speedlimit', 'crosswalk', 'trafficlight']
THICKNESS = 2
CUSTOM_CONFIG = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
