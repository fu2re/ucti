import pytest

from get_final_url import get_final_url as get_final_url_command


@pytest.fixture()
def get_final_url():
    def get_final_url_(url, depth=2, method='head', payload=None, headers=None):
        return get_final_url_command.callback(
            url=f'http://localhost:8000/{url.lstrip("/")}',
            depth=depth,
            method=method,
            payload=payload or {},
            headers=headers or {}
        )
    return get_final_url_
