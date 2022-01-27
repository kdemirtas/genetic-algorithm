import os
import json

from genetic_algorithm.utils.helpers import *
from genetic_algorithm.classes.settings import Settings
from genetic_algorithm.classes.directory_structure import DirectoryStructure


class Model:
    def __init__(self):
        self.ds = DirectoryStructure()

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, settings_dict):
        self._settings = Settings(settings_dict)

    def _parse_settings(self):
        settings_file_path = os.path.join(self.ds.DATA_DIR, 'settings.json')
        parse_result = json_parser(settings_file_path)
        self.settings = parse_result

        return parse_result