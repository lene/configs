from typing import List

__author__ = 'Lene Preuss <lene.preuss@gmail.com>'

from hashlib import md5
from os.path import join

from .temp_dir_test_case import TempDirTestCase


class TestJunkFilenames(TempDirTestCase):

    def create_files(self, template: str, number: int):
        self.files: List[str] = []
        for i in range(1, number+1):
            filename = template.format(i, md5(str(i).encode('utf-8')).hexdigest())
            path = join(self.testdir.name, filename)
            self.create_file(path)
            self.files.append(path)
