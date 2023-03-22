import numpy as np
class ImageProcessor:
    def __init__(self, image, trim_size=10):
        self.image = image
        self.trim_size = trim_size
        self.wDetect = False

    def process(self):
        result = self.trim_image()
        if self.wDetect:
            return result
        else:
            return result
        
    def trim_image(self):
        if self.image is None:
            raise ValueError("Görüntü yüklenemedi.")
        h, w, c = self.image.shape
        left_white = 0
        for i in range(w):
            if np.mean(self.image[:, i]) > 127:
                left_white += 1
            else:
                break
        right_white = 0
        for i in range(w-1, -1, -1):
            if np.mean(self.image[:, i]) > 127:
                right_white += 1
            else:
                break
    
        if left_white > 20 and right_white > 20:
            new_w = w - (left_white + right_white + self.trim_size*2)
            if new_w < w/6:
                self.image = self.image.copy()  # make a copy of the original image
                self.wDetect = False
            else:
                self.wDetect = True
                self.image[:, :left_white+self.trim_size] = 150  # paint the left area with gray
                self.image[:, w-right_white-self.trim_size:] = 150  # paint the right area with gray
        elif left_white > 20:
            new_w = w - (left_white + self.trim_size)
            if new_w < w/6:
                self.image = self.image.copy()
                self.wDetect = False
            else:
                self.wDetect = True
                self.image[:, :left_white+self.trim_size] = 150  # paint the left area with gray
        elif right_white > self.trim_size:
            new_w = w - (right_white + self.trim_size)
            if new_w < w/6:
                self.image = self.image.copy()
                self.wDetect = False
            else:
                self.wDetect = True
                self.image[:, w-right_white-self.trim_size:] = 150  # paint the right area with gray
        else:
            self.wDetect = False
    
        if not self.wDetect:
            return self.image
        else:
            return self.image

    
