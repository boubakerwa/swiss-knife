## file summary

import tensorflow as tf
from collections import defaultdict
from typing import Optional, Tuple

from unit_test_utils import is_config


class TF_model():
    '''
    class for creating either Serial of Functional tf2 models
    '''

    def __init__(self, name: str, config: Optional[dict]=None, \
        API_TYPE: str='sequential'):
        assert API_TYPE.lower() in ['sequential', 'functional'], 'only' \
            + ' sequential and functional accepted as API_TYPE.'
        
        self._API_TYPE = API_TYPE

        if config is None:
                self._config = self.create_base_config(model_name=name, \
                    API_TYPE=API_TYPE)
        else:
            self._config = config

    def create_base_config(self, model_name: str, API_TYPE: str, \
        batch_input_shape: Optional(Tuple[Optional[int],...])=None) -> dict:

        if API_TYPE=='sequential':
            config={'name': model_name, \
                'layers': defaultdict(list)}
            input_layer = {'class_name': 'InputLayer', \
                'config':{'batch_input_shape': batch_input_shape, \
                    'dtype': tf.float32,
                    'sparse': False,
                    'ragged': False,
                    'name': 'input_layer'}}
            config['layers'].append(input_layer)
            return config
        else:
            raise NotImplementedError

    def update_config(self, config: dict) -> None:
        assert is_config(config)
        self._config = config

    def create_model(self):
        if self._API_TYPE == 'sequential':
            self.model = tf.keras.models.Sequential.from_config(self._config)
        else:
            self.model = tf.keras.models.Model.from_config(self._config)
