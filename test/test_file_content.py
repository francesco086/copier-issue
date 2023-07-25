from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

import copier


class TestFileContent(TestCase):
    def setUp(self) -> None:
        self.init_template_values()
        self.tmpdir = TemporaryDirectory()
        self.use_copier()

    def tearDown(self) -> None:
        return self.tmpdir.cleanup()
    
    def test_destination_folder_exits(self):
        assert Path(self.tmpdir.name).exists()

    @staticmethod
    def get_template_path() -> Path:
        return Path(__file__).parent.parent / "src"

    def use_copier(self):
        copier.run_copy(
            self.get_template_path().as_posix(),
            self.tmpdir.name,
            data=self.get_example_answers(),
        )

    def get_example_answers(self) -> dict:
        return {}

    def init_template_values(self):
        pass
