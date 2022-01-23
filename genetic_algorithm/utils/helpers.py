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