import cv2
from cvzone.FaceDetectionModule import FaceDetector


# Class created
class CameraDetection:
    def __init__(self):
        self.__video     = cv2.VideoCapture(0)  # standard webcam
        self.__detector  = FaceDetector()       # This will detected your face


    # Show camera in your window
    def CameraShow(self) -> None:
        _, img    = self.__video.read()
        img, boxe = self.__detector.findFaces(img, draw=True)
        
        cv2.imshow('Result', img)
        if cv2.waitKey(1) == 27:
            return
        self.CameraShow()