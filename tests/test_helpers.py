import os
import unittest

import numpy as np

from genetic_algorithm.utils import helpers as hp


class TestHelpers(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_helpers_enure_np_array_for_nparray(self):
        arr = np.array([1, 2, 3])
        nparr = hp.ensure_np_array(arr)
        self.assertIsInstance(nparr, np.ndarray)

    def test_helpers_enure_np_array_for_python_list(self):
        plist = [1, 2, 3]
        nparr = hp.ensure_np_array(plist)
        self.assertIsInstance(nparr, np.ndarray)

    def test_helpers_enure_np_array_for_python_tuple(self):
        ptuple = (1, 2, 3)
        nparr = hp.ensure_np_array(ptuple)
        self.assertIsInstance(nparr, np.ndarray)
    
    def test_helpers_enure_np_array_for_unsupported_type(self):
        pstring = "Unsupported"
        pint = 7
        with self.assertRaises(TypeError):
            hp.ensure_np_array(pstring)
        with self.assertRaises(TypeError):
            hp.ensure_np_array(pint)
        


    


if __name__ == "__main__":
    unittest.main()
