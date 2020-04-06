import pytest
import myapp
import config
from unittest.mock import patch


@pytest.fixture(scope="session")
def celery_config():
    return config.celery_config


def test_hello(celery_worker):
    assert myapp.hello() == "HELLO HELLO HELLO HELLO"


def test_hello_patched():
    with patch("myapp.hello_task") as mock_task:
        mock_task.delay.return_value.wait.return_value = "ok"
        assert myapp.hello() == "OK"
