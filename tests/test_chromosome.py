import os
import unittest
import json


class TestInitializer(unittest.TestCase):

    def setUp(self):
        self.ds = directory.DirectoryStructure()
        self.test_data_file = os.path.join(self.ds.test_data_dir, 'input_data_3_checkpoints.json')
        self.ini = initializer.Initializer(self.test_data_file)

    def tearDown(self):
        pass

    def test_chromosome(self):
        pass



if __name__ == "__main__":
    unittest.main()