import os
import sys

class DirectoryStructure:
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.TESTS_DIR = os.path.join(self.ROOT_DIR, 'tests')
        self.DATA_DIR = os.path.join(self.ROOT_DIR, 'data')
        self.FILES_DIR = os.path.join(self.ROOT_DIR, 'files')