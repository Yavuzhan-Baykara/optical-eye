from PIL import Image
import imagehash
import numpy as np
from matplotlib import cm
import cv2


def compare_images(img1, img2):
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)

    hash0 = imagehash.dhash(img1) 
    hash1 = imagehash.dhash(img2)
    cutoff = 20  # maximum bits that could be different between the hashes. 
    if hash0 - hash1 < cutoff:
        return True
    else:
        return False
