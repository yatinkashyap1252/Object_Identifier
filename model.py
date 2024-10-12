import PIL.Image
from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL
from PIL import Image

class Model:
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = []
        class_list = []

        for i in range(1, counters[0]):
            img = cv.imread(f"1/frame{i}.jpg")[:,:,0]
            img = cv.resize(img, (130, 130)) 
            img = img.reshape(16900)
            img_list.append(img)
            class_list.append(1)
        
        for i in range(1, counters[1]):
            img = cv.imread(f"2/frame{i}.jpg")[:,:,0]
            img = cv.resize(img, (130, 130)) 
            img = img.reshape(16900)
            img_list.append(img)
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        if len(img_list) == 0 or len(class_list) == 0:
            print("Error: Empty image or class list")
            return

        self.model.fit(img_list, class_list)
        print("Model successfully trained")

    def predict(self, frame):
        frame = frame[1]
        cv.imwrite('frame.jpg', cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = PIL.Image.open('frame.jpg')
        img.thumbnail((130, 130), Image.Resampling.LANCZOS)
        img.save("frame.jpg")
        img = cv.imread('frame.jpg')[:,:,0]

        if img.shape != (130,130):
            img=cv.resize(img,(130,130))
        
        img = img.reshape(16900)                #this will make array and this is showing the size or the total content in it 130*130

        prediction = self.model.predict([img])  # Pass img as a list

        return prediction[0]