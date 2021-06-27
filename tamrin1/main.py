# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtUiTools import QUiLoader

# from threading import Thread
from PySide6.QtCore import QThread,Signal,Qt
from PySide6.QtWidgets import *

from PySide6.QtGui import QPixmap,QImage
import cv2


# convert an opencv image to Qpixmap
def ConvertCvimage2Qtimage(cv_image):
    # cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    height,width, channel = cv_image.shape
    # bytesperline=3*width
    qimg=QImage(cv_image.data,width,height,QImage.Format_BGR888)
    return QPixmap.fromImage(qimg)

class FaceDetector(QThread):
    signal_success_process=Signal(object)
    def __init__(self,image_path):
        super(FaceDetector, self).__init__()
        self.image_path=image_path
    def run(self):
        face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        my_video=cv2.VideoCapture(self.image_path)
        while True:
            ret,frame=my_video.read()
            if not ret:
                break
            frame_gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            faces=face_detector.detectMultiScale(frame_gray,1.3)
            for i,face in enumerate(faces):
                x,y,w,h=face
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),8)
                # cv2.imwrite('out.jpg',image)
            # img_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.signal_success_process.emit(frame)

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        self.ui.btn_browse.clicked.connect(self.openImage)
        self.ui.btn_start.clicked.connect(self.startfacedetection)
        self.ui.btn_Screenshot.clicked.connect(self.Take_Screenshot)

    def openImage(self):
        image_path=QFileDialog.getOpenFileName(self,'open your image')
        self.image_path=image_path[0]
        self.ui.lineEdit_image_path.setText(self.image_path)
        my_pixmap=QPixmap(self.image_path)
        self.ui.label_image.setPixmap(my_pixmap)
    def startfacedetection(self):
        self.face_detector=FaceDetector(self.image_path)
        self.face_detector.start()
        self.face_detector.signal_success_process.connect(self.showoutput)
    def showoutput(self,image):
        # my_pixmap=QPixmap('out.jpg')
        my_pixmap=ConvertCvimage2Qtimage(image)
        self.ui.label_image.setPixmap(my_pixmap)

    def Take_Screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.ui.label_screen.setPixmap(self.preview_screen.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        img, _ = QFileDialog.getSaveFileName(self, "Save your image")
        self.preview_screen.save(img)
        self.ui.label_screen.hide()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
