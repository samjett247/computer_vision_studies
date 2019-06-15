from scipy.optimize import minimize
from scipy.ndimage import filters
import numpy as np

def denoise(im,lamda=100):
    """ An implementation of the Rudin-Osher-Fatemi (ROF) denoising model
        using the numerical procedure presented in Eq. (11) of A. Chambolle
        (2005). Implemented using periodic boundary conditions.
        
        Input: noisy input image (grayscale), initial guess for U, weight of 
        the TV-regularizing term, steplength, tolerance for the stop criterion
        
        Output: denoised and detextured image, texture residual. """
    if len(im.shape)>2:
        raise Exception('Convert to grayscale first')
    # J, i.e. the total variance
    def J(im):
        imx, imy = np.zeros(im.shape),np.zeros(im.shape)
        filters.sobel(im,1,imx)
        filters.sobel(im,0,imy)
        stacked = np.stack((imx,imy))
        return np.sum(np.linalg.norm(stacked, axis=2), axis=(0,1))
    
    # Cost according to ROF model
    def cost(U,im, lamda, J):
        U = np.reshape(U, im.shape)
        return np.linalg.norm(U-im)**2 + 2*lamda*J(U)
    
    soln = minimize(cost, im, args=(im, lamda, J))
    return soln

if __name__ == '__main__':
    print('go puck yourself - Michael Scott')