import json

import numpy as np


def ensure_np_array(arr):
    """
    Takes arr as input and makes sure the array type is numpy.array. If it is not,
    converts it to a numpy array.
    Args:
        arr -> An array-like object
    Returns:
        nparr -> Numpy array
    """
    if isinstance(arr, np.ndarray):
        nparr = arr
    elif isinstance(arr, list):
        nparr = np.array(arr)
    elif isinstance(arr, tuple):
        nparr = np.array(arr)
    else:
        raise(TypeError("Unsupported type for numpy array"))

    return nparr

def json_parser(file_path):
    extension = file_path.split('.')
    if extension[1] != 'json':
        raise(TypeError('Input file does not have .json extension.'))
    with open(file_path) as fp:
        parse_result = json.load(fp)

    return parse_result