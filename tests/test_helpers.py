import os
import unittest

import numpy as np

from genetic_algorithm.utils import helpers as hp


class TestHelpers(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_helpers_ensure_np_array_for_nparray(self):
        arr = np.array([1, 2, 3])
        nparr = hp.ensure_np_array(arr)
        self.assertIsInstance(nparr, np.ndarray)

    def test_helpers_ensure_np_array_for_python_list(self):
        plist = [1, 2, 3]
        nparr = hp.ensure_np_array(plist)
        self.assertIsInstance(nparr, np.ndarray)

    def test_helpers_ensure_np_array_for_python_tuple(self):
        ptuple = (1, 2, 3)
        nparr = hp.ensure_np_array(ptuple)
        self.assertIsInstance(nparr, np.ndarray)
    
    def test_helpers_ensure_np_array_for_unsupported_type(self):
        pstring = "Unsupported"
        pint = 7
        with self.assertRaises(TypeError):
            hp.ensure_np_array(pstring)
        with self.assertRaises(TypeError):
            hp.ensure_np_array(pint)

    def test_helpers_ensure_np_array_for_2d_list(self):
        plist = [[1, 2], [3, 4], [5, 6]]
        nparr = hp.ensure_np_array(plist)
        nrows = len(plist)
        ncols = len(plist[0])
        shape = tuple([nrows, ncols])
        self.assertEqual(shape, nparr.shape)

    def test_helpers_ensure_np_array_for_3d_list(self):
        plist = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]
        nparr = hp.ensure_np_array(plist)
        n1st = len(plist)
        n2nd = len(plist[0])
        n3rd = len(plist[0][0])
        shape = tuple([n1st, n2nd, n3rd])
        self.assertEqual(shape, nparr.shape)

    def test_helpers_json_parser(self):
        file_path = 'bad_file.xlsx'
        with self.assertRaises(TypeError):
            hp.json_parser(file_path)
        

if __name__ == "__main__":
    unittest.main()
