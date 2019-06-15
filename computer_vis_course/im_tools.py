import os
import numpy as np
from PIL import Image

def get_list_of_images(path):
    '''
    Returns a list of valid JPEG files in 
    path argument.
    '''
    return [os.path.join(path,f.lower()) for f in os.listdir(path) if (f[-4:].lower() == '.jpg')]
    
def histeq(im,nbr_bins=256):
    """ 
    Histogram equalization of a grayscale image.
    Takes im as np array
    """
    # get image histogram
    imhist,bins = np.histogram(im.flatten(),nbr_bins,density=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize
    # use linear interpolation of cdf to find new pixel values
    im2 = np.interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf
    
def imresize(im,sz):
    """ 
    Resize an image array using PIL. 
    Takes im as np.array
    """
    pil_im = Image.fromarray(im.astype('uint8'))
    return np.array(pil_im.resize(sz))

if __name__=='__main__':
    print(get_list_of_images(os.path.join(os.getcwd(), 'samples')))