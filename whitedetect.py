import numpy as np
class ImageProcessor:
    def __init__(self, image, trim_size=10):
        self.image = image
        self.trim_size = trim_size
        self.wDetect = False
        self.area = None
        _, self.out_w, _ = image.shape

    def trim_image(self, tolerance=60):
        if self.image is None:
            raise ValueError("Görüntü yüklenemedi.")
        h, w, c = self.image.shape
        left_white = 0
        for i in range(w):
            if np.mean(self.image[:, i]) > 127:
                left_white += 1
            elif np.min(self.image[:, i]) >= 127 - tolerance:
                left_white += 1
            else:
                break
        right_white = 0
        for i in range(w-1, -1, -1):
            if np.mean(self.image[:, i]) > 127:
                right_white += 1
            elif np.min(self.image[:, i]) >= 127 - tolerance:
                right_white += 1
            else:
                break
        
        if left_white > 20 and right_white > 20:
            new_w = w - (left_white + right_white + self.trim_size*2)
            if new_w < w/1000:
                return self.image, None
            else:
                self.wDetect = True
                self.image[:, :left_white+self.trim_size] = 150  # paint the left area with gray
                self.image[:, w-right_white-self.trim_size:] = 150  # paint the right area with gray
        elif left_white > 20:
            new_w = w - (left_white + self.trim_size)
            if new_w < w/1000:
                return self.image, None
            else:
                self.wDetect = True
                self.image[:, :left_white+self.trim_size] = 150  # paint the left area with gray
        elif right_white > self.trim_size:
            new_w = w - (right_white + self.trim_size)
            if new_w < w/1000:
                return self.image, None
            else:
                self.wDetect = True
                self.image[:, w-right_white-self.trim_size:] = 150  # paint the right area with gray
        if not self.wDetect:
            return self.image, w
        else:
            self.out_w = new_w
            return self.image, self.out_w

    def paint_left_gray(self):
        h, w, c = self.image.shape
        self.image[:, :self.trim_size] = 150
        return self.image
    def paint_right_gray(self):
        h, w, c = self.image.shape
        self.image[:, w-self.trim_size:] = 150
        return self.image

    
