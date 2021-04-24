'''
file description
'''
import os
import zipfile
from logging_utils import myLogger
import numpy as np

# typing
from typing import Tuple

# tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# config
import json

class Data_Utils():
    '''
    python object for io of all types of data.
    '''

    def __init__(self, base_dir: str, data_format: str, data_type: str,\
        logging: bool = True):

        ### LOGGING ###
        self.logging=logging
        # create logger
        if logging:
            self.logger = myLogger("data_logger")
            self.logger.add_info_handler("data_info.log") # warning handler not working yet
        

        _ = self.set_paths(base_dir)
        
        ### TESTS ###
        supported_data_types = ['image', 'text', 'audio', 'audio/image']
        assert data_type.lower() in supported_data_types, f'unsupported data \
            type. Available types: {supported_data_types}'

        supported_image_formats = ['png', 'jpg', 'jpeg']

        if data_type=='image':
            assert data_format.lower() in supported_image_formats, f'unsupported \
                image format. Available formats: {supported_image_formats}'

        if data_type=='text':
            raise NotImplementedError

        if data_type=='audio':
            raise NotImplementedError

        if data_type=='audio/image':
            raise NotImplementedError

        

    def log_info(self, message):
        '''
        checks if logging is on, logs message into info
        '''
        if self.logging:
            self.logger.logger.info(message)

    def log_warn(self, message):
        '''
        checks if logging is on, logs message into warnings
        '''
        if self.logging:
            self.logger.logger.warn(message)

    def unzip(self, filepath, out_dir=os.sep+'tmp'):
        assert filepath.endswith('.zip'), 'only .zip files supported.'

        zip_ref = zipfile.ZipFile(local_zip, 'r')

        zip_ref.extractall(out_dir)
        zip_ref.close()
        self.log_info(f'extracted data files into {out_dir}')
        return True

    def set_paths(self, base_dir):
        '''
        update saved paths for data for base-train/test/val repo structure
        '''
        assert os.path.isdir(base_dir), 'please enter a valid base_dir path.'
        self.base_dir = base_dir
        self.train_dir = os.path.join(base_dir, 'train')
        self.test_dir = os.path.join(base_dir, 'test')
        self.validation_dir = os.path.join(base_dir, 'validation')
        self.log_info(f'updated base_dir: {base_dir}')
        return True

    def create_keras_ImgGen(self, rescale: np.float32 = 1./255., \
        batch_size: int = 20, class_mode: str = 'binary', \
            target_size: Tuple[int, int] = (150, 150) ):

        assert os.path.isdir(self.base_dir), 'please set a basedir.'
        assert os.path.isdir(self.train_dir), 'Data on disk has to follow\
             the following structure: base -> train/validation/(test)'
        assert rescale>0 and rescale<=1., 'rescaling value has to be \
            between 0 and 1'
        train_datagen = ImageDataGenerator(rescale=rescale)
        self.train_generator = train_datagen.flow_from_directory(self.train_dir,
                                                    batch_size=batch_size,
                                                    class_mode=class_mode,
                                                    target_size=target_size)

        if os.path.isdir(self.test_dir):
            test_datagen = ImageDataGenerator(rescale=rescale)
            self.test_generator = test_datagen.flow_from_directory(self.test_dir,
                                                    batch_size=batch_size,
                                                    class_mode=class_mode,
                                                    target_size=target_size)
        if os.path.isdir(self.validation_dir):
            validation_datagen = ImageDataGenerator(rescale=rescale)
            self.validation_generator = validation_datagen.flow_from_directory(self.validation_dir,
                                                    batch_size=batch_size,
                                                    class_mode=class_mode,
                                                    target_size=target_size)
            
    def read_tf_config(self, path):
        with open(path, 'r') as fp:
            conf = json.load(fp)
        return conf
        