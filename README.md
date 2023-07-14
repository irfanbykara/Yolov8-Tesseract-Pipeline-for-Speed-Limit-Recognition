# Yolov8-Tesseract-Pipeline-for-Speed-Limit-Recognition
**This is a python project that recognizes traffic speed limits on the road using ensemble of object detection and ocr techniques.**

This project uses pytorch model that has been trained with yolov8 to detect traffic signs, explicitly speed limit signs. The model is obtained after 200 epochs. 
After detecting the speed limit signs in the video, process_for_ocr function is called to do some preprocessing for OCR engine to work correctly.


## To run

```
pip install -r requirements.txt
python speed_limit_pipeline.py  --path 'youtube_url_for_your_video'

```

It is also possible to run the main function with a static video. For this you can pass --static argument with --path 'respective_static_path'


Please note that you have to install tesseract.exe file and give the path in consts_sample.py file.

https://github.com/irfanbykara/Yolov8-Tesseract-Pipeline-for-Speed-Limit-Recognition/assets/63783207/acbf2884-2a09-477d-b02b-70a61ab72357

