import os
import unittest

from genetic_algorithm.classes.directory_structure import DirectoryStructure as ds
from genetic_algorithm.utils.model import Model

class TestModel(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def tearDown(self):
        pass

    def test_model_parse_settings(self):
        parse_results = self.model._parse_settings()
        self.assertEqual(parse_results['test_check_num'], 777)