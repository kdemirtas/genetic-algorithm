import os
import unittest

from genetic_algorithm.classes.directory_structure import DirectoryStructure as ds

class TestDirectoryStructure(unittest.TestCase):

    def setUp(self):
        self.d = ds()
        self.ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    def tearDown(self):
        pass

    def test_directory_structure_root(self):
        self.assertEqual(self.ROOT_DIR, self.d.ROOT_DIR)