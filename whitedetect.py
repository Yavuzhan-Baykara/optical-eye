import numpy as np
class ImageProcessor:
    def __init__(self, image, trim_size=10, choise=""):
        self.image = image
        self.trim_size = trim_size
        self.wDetect = False
        self.area = None
        _, self.out_w, _ = image.shape
        self.choise = choise

    def trim_image(self, tolerance=60):
        if self.image is None:
            raise ValueError("Görüntü yüklenemedi.")
        h, w, c = self.image.shape
        left_white = 0
        left_count = 0
        for i in range(w):
            if np.mean(self.image[:, i]) > 127:
                left_white += 1
                left_count = 0
            elif np.min(self.image[:, i]) >= 127 - tolerance:
                left_white += 1
                left_count = 0
            else:
                left_count += 1
                if left_count >= 50:
                    break
        right_white = 0
        right_count = 0
        for i in range(w-1, -1, -1):
            if np.mean(self.image[:, i]) > 127:
                right_white += 1
                right_count = 0
            elif np.min(self.image[:, i]) >= 127 - tolerance:
                right_white += 1
                right_count = 0
            else:
                right_count += 1
                if right_count >= 50:
                    break
        
        if self.choise == "left":
            new_w = w - (left_white + self.trim_size)
            self.wDetect = True
            self.image[:, :left_white+self.trim_size] = 150  # paint the left area with gray
        if self.choise == "right":
            new_w = w - (right_white + self.trim_size)
            self.wDetect = True
            self.image[:, w-right_white-self.trim_size:] = 150  # paint the right area with gray
            
        if not self.wDetect:
            return self.image, w
        else:
            self.out_w = new_w
            return self.image, self.out_w

    # def paint_left_gray(self):
    #     h, w, c = self.image.shape
    #     self.image[:, :self.trim_size] = 150
    #     return self.image
    # def paint_right_gray(self):
    #     h, w, c = self.image.shape
    #     self.image[:, w-self.trim_size:] = 150
    #     return self.image

    
