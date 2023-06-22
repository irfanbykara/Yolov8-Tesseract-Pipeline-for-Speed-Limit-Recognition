import pafy
import cv2
from ultralytics import YOLO
import pytesseract
from process_for_ocr import *
import time
from consts import *
import argparse
import os


def main(is_static, path, verbose):

    print(is_static,path,verbose)
    model = YOLO(MODEL_PATH)

    if not is_static:

        url = path
        video = pafy.new(url)

        best = video.getbest(preftype="mp4")
        cap = cv2.VideoCapture()  # Youtube
        cap.open(best.url)

    else:
        cap = cv2.VideoCapture(path)

    os.environ['TESSDATA_PREFIX'] = PYTESSARACT_PATH
    os.environ['TESSDATA_PREFIX'] = TESSDATA_CONFIG

    speed_limit = 'Unknown'
    p_time = 0

    while True:

        success, img = cap.read()
        results = model.predict(img)

        results = results[0].boxes.data
        cv2.namedWindow("Region of Interest Processed", cv2.WINDOW_NORMAL)


        for result in results:
            if CLASSES[int(result[5])] == 'speedlimit':

                x = int(result[0])
                y = int(result[1])

                x2 = int(result[2])
                y2 = int(result[3])

                cropped_img = img[y:y2,x:x2]
                masked = crop_circle_with_text(cropped_img)

                if masked is not None:


                    try:

                        text = pytesseract.image_to_string(masked, lang='eng', \
                                                           config=CUSTOM_CONFIG)
                        if text != '' and text != None:

                            speed_limit = text

                            if (verbose):

                                # Using resizeWindow()
                                cv2.resizeWindow("Region of Interest Processed", 300, 300)

                                cv2.imshow('Region of Interest Processed', masked)

                    except Exception as e:
                        print(e)

                cv2.rectangle(img, (x, y), (x2, y2), WHITE_COLOR, THICKNESS)

        c_time = time.time()
        fps = 1 / (c_time - p_time)

        p_time = c_time
        cv2.putText(img, 'FPS: ' + str(int(fps)),
                    (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.putText(img, f'Current speed limit is: {speed_limit}', (300, 50), FONT, 1, BLACK_COLOR, THICKNESS, )
        cv2.imshow( 'Traffic Sign Recognizer', img )

        cv2.waitKey( 1 )

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script so useful.')

    parser.add_argument('--static', action='store_true')
    parser.add_argument("--path",type=str,default='https://www.youtube.com/watch?v=L0eY0FfQ1rs')
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args()

    is_static = args.static
    path = args.path
    verbose = args.verbose

    main(is_static,path,verbose)


