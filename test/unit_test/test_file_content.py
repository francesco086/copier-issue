from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from unittest import TestCase

import copier


class TestFileContent(TestCase):
    docker_image_name = "test_image"

    def setUp(self) -> None:
        self.init_template_values()
        self.tmpdir = TemporaryDirectory()
        self.use_copier()

    def tearDown(self) -> None:
        return self.tmpdir.cleanup()

    def test_destination_folder_exits(self):
        assert Path(self.tmpdir.name).exists()

    def test_gitlab_ci_file_exists(self):
        assert (Path(self.tmpdir.name) / ".gitlab-ci.yml").exists()

    def test_deploy_file_exists(self):
        assert (Path(self.tmpdir.name) / "helper-scripts/deploy-prod-image.sh").exists()

    def test_deploy_test_file_exists(self):
        assert (Path(self.tmpdir.name) / "helper-scripts/deploy-test-image.sh").exists()

    def test_sample_dockerfile_exists(self):
        assert (Path(self.tmpdir.name) / "Dockerfile").exists()

    def test_sample_test_exists(self):
        assert (Path(self.tmpdir.name) / "test.sh").exists()

    def test_sample_determine_docker_image_tags_exists(self):
        assert (Path(self.tmpdir.name) / "determine-docker-image-tags.sh").exists()

    def test_answer_file_exists(self):
        assert (Path(self.tmpdir.name) / ".copier-answers.yml").exists()

    def test_determine_docker_image_tags_returns_a_non_empty_string(self):
        output = run(
            [
                "sh",
                (Path(self.tmpdir.name) / "determine-docker-image-tags.sh").as_posix(),
            ],
            check=True,
            capture_output=True,
        )
        assert output.stdout.decode("utf-8") != ""

    def test_docker_image_name_is_used_in_gitlab_ci_file(self):
        file_content = (Path(self.tmpdir.name) / ".gitlab-ci.yml").read_text()
        assert f"docker image build -t {self.docker_image_name}" in file_content

    def test_docker_image_name_is_used_in_deploy_file(self):
        file_content = (
            Path(self.tmpdir.name) / "helper-scripts/deploy-prod-image.sh"
        ).read_text()
        assert "{{ docker_image_name }}" not in file_content

    def test_docker_image_name_is_used_in_deploy_test_file(self):
        file_content = (
            Path(self.tmpdir.name) / "helper-scripts/deploy-test-image.sh"
        ).read_text()
        assert "{{ docker_image_name }}" not in file_content

    @staticmethod
    def get_template_path() -> Path:
        return Path(__file__).parent.parent.parent

    def use_copier(self):
        copier.run_copy(
            self.get_template_path().as_posix(),
            self.tmpdir.name,
            data=self.get_example_answers(),
        )

    def get_example_answers(self) -> dict:
        return {"docker_image_name": self.docker_image_name}

    def init_template_values(self):
        pass
