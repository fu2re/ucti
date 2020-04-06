import pytest


def test_index(client):
    assert client.get('/').status_code == 200


def test_single(client):
    assert client.get('/1/').status_code == 302


@pytest.mark.parametrize(
    'depth',
    (
        2, 3, 4999
    )
)
def test_multiple(client, depth):
    assert client.get(f'/{depth}/').status_code == 302


def test_infinite(client):
    assert client.get('/inf/').status_code == 302


def test_infinite_response(client):
    assert client.get('/inf/').status_code == 302
