import pytest

MSG_SUCCESS = 'The final url is'
MSG_DEEP = 'Too many redirects'
MSG_UNEXPECTED = 'Url response with status'
MSG_RESTRICTED = 'Method does not allowed'


@pytest.mark.parametrize(
    'method',
    ('get', 'post', 'head')
)
@pytest.mark.parametrize(
    'url,depth,msg',
    (
        ('/', 2, MSG_SUCCESS),
        ('/1/', 2, MSG_SUCCESS),
        ('/2/', 2, MSG_SUCCESS),
        ('/3/', 2, MSG_DEEP),
        ('/3/', 3, MSG_SUCCESS),
        ('/499/', 2, MSG_DEEP),
        ('/inf/', 2, MSG_DEEP),
        ('/bafbadf/', 2, MSG_UNEXPECTED),
    )
)
def test_command(get_final_url, capsys, method, url, depth, msg):
    get_final_url(url, depth, method)
    captured = capsys.readouterr()
    assert msg in captured.out


def test_restricted_method(get_final_url, capsys):
    get_final_url('/', method='connect')
    captured = capsys.readouterr()
    assert MSG_RESTRICTED in captured.out
