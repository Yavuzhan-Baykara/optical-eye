class ImageProcessor:
    def __init__(self, image, trim_size=10):
        self.image = image
        self.trim_size = trim_size
        self.wDetect = False

    def process(self):
        return self.trim_image()
        
    def trim_image(self):
        if self.image is None:
            raise ValueError("Görüntü yüklenemedi.")
        h, w, c = self.image.shape
        left_white = 0
        for i in range(w):
            if 255 in self.image[:, i, :]:
                left_white += 1
            else:
                break
        right_white = 0
        for i in range(w-1, -1, -1):
            if 255 in self.image[:, i, :]:
                right_white += 1
            else:
                break

        if left_white > 20 and right_white > 20:
            self.wDetect = True
            self.image = self.image[:, left_white+self.trim_size:w-right_white-self.trim_size, :]
        elif left_white > 20:
            self.wDetect = True
            self.image = self.image[:, left_white+self.trim_size:, :]
        elif right_white > self.trim_size:
            self.wDetect = True
            self.image = self.image[:, :w-right_white-self.trim_size, :]
        return self.image, self.wDetect