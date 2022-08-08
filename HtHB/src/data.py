import pathlib
import pandas as pd

LOCAL_GDRIVE = '/mnt/g/My Drive/Dev/datasets/hubmap-organ-segmentation'
LOCAL_CDRIVE = '/mnt/c/dev/datasets/hubmap-organ-segmentation'

def get_data_path(env, folder='base'):
    '''
    get data path of a specific folder as a string
    
    parameters:
        env -> 'local' or 'remote'
        folder -> 'base', 'test_images', 'train_images' or 'train_annotations'
    '''
    if env == 'cdrive':
        gdrive = pathlib.Path(LOCAL_CDRIVE)
    elif env == 'gdrive':
        gdrive = pathlib.Path(LOCAL_GDRIVE)
    if folder=='base':
        return str(gdrive)
    elif folder=='test_images':
        return str(gdrive / 'test_images')
    elif folder=='train_images':
        return str(gdrive / 'train_images')
    elif folder=='train_annotations':
        return str(gdrive / 'train_annotations')
    