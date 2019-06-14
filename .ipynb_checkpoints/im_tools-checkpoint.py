import os

def get_list_of_images(path):
    '''
    Returns a list of valid JPEG files in 
    path argument.
    '''
    return [os.path.join(path,f.lower()) for f in os.listdir(path) if (f[-4:].lower() == '.jpg')]
    
if __name__=='__main__':
    print(get_list_of_images(os.path.join(os.getcwd(), 'samples')))