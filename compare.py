from PIL import Image
from imagehash import dhash 

def compare_images(img1, img2, cutoff=20):
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)
    hash0 = dhash(img1) 
    hash1 = dhash(img2)
    
    

    if hash0 - hash1 < cutoff:
        return True
    else:
        return False
    
