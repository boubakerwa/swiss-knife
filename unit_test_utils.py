def is_config(config: dict) -> bool:
    assert list(config.keys()) == ['name', 'layers'] ,\
        'config top keys should be name and layers'
    for layer in config['layers']:
        assert type(layer) == dict, \
            'layers should be passed as dicts'
        assert list(layer.keys()) == ['class_name',
                                'config'], \
            'layers should only contain class_name \
                and config as keys'
        assert type(layer['config']) == dict, \
            'layer config should be a dict'