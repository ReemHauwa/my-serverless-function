### test_main.py

import json
from unittest.mock import Mock
import main

def test_process_input_json():
    data = {'name': 'Test'}
    req = Mock(get_json=Mock(return_value=data), args={})
    
    response = main.process_input(req)
    assert response == 'Hello Test! Your input has been processed.'

def test_process_input_default():
    req = Mock(get_json=Mock(return_value=None), args={})
    
    response = main.process_input(req)
    assert response == 'Hello World! Your input has been processed.'
