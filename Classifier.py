import cv2 as cv

class camera:
    def __init__(self):
        self.camera = cv.VideoCapture(0)  #'0' is written because i have only one camera if you have more than one write 1,2,3,etc
        self.width=self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height=self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera!")
        
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
        
    def get_frame(self):
        if self.camera.isOpened():
            ret,frame =self.camera.read()

            if ret:
                return(ret,cv.cvtColor(frame,cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
            
        else:
            return None