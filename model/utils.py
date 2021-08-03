import numpy as np
import cv2

def preprocess_input(img, w, h, display_format=False):
    ih, iw, _ = img.shape
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    image_data = cv2.resize(img, (nw,nh))
    new_image = np.full((h,w,3), (128,128,128), dtype='uint8')
    new_image[(h-nh)//2 : (h+nh)//2, (w-nw)//2:(w+nw)//2] = image_data
    image_data = new_image.astype('float')/255.0
    if not display_format:
        image_data = image_data[np.newaxis, ...]

    return image_data