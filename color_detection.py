import cv2
import numpy as np

video_cap=cv2.VideoCapture(0)

w=int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
video_writer=cv2.VideoWriter('myclip.mp4',fourcc,30,(w,h))

alpha=2
beta=50
while True:
    ret,frame=video_cap.read()
    if not ret:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    w,h=frame.shape
    roi=frame[w//2-100:w//2+100,h//2-100:h//2+100]
    roi=cv2.add(cv2.multiply(roi,alpha),beta)
    roi_optimized=cv2.equalizeHist(roi)
    average=np.average(roi_optimized)

    if average<80:
        print('black')
    elif average <=160:
        print('gray')
    else:
        print('white')
    frame_blur=cv2.blur(frame,(35,35))
    frame_blur[w//2-100:w//2+100,h//2-100:h//2+100]=roi_optimized
    cv2.imshow('output',frame_blur)
    video_writer.write(frame)
    if cv2.waitKey(1)==ord('q'):
        break
    # cv2.waitKey(1)
video_cap.release()
video_writer.release()