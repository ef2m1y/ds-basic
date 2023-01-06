import numpy as np

def crop_img(im, crop_size=120):
    '''
    Cut off crop_size around the crop_size
    
    Params
    ----------------
        im: image (NumPy Array)
        crop_size: crop size (int)
    
    Returns
    ----------------
        im: croped image (NumPy Array)
        
    '''
    
    im = im[crop_size:-crop_size, crop_size:-crop_size,  :]
    
    return im