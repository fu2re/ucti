#!/usr/bin/env python
import requests
import click
from requests import TooManyRedirects


# more methods produces more edge cases, so only basic methods is supported
# as example delete requests can return a non-200 http status
ALLOWED_METHODS = (
    'head',
    'get',
    'post',
)


@click.command()
@click.option('--depth', default=2, help='Maximum recursion depth')
@click.option('--method', default='head', help='Request Method')
@click.option('--payload', default=None, help='Payload', type=dict)
@click.option('--headers', default=None, help='Headers', type=dict)
@click.argument('url')
def get_final_url(url, depth, method, payload, headers):
    payload = payload or {}
    headers = headers or {}
    if method.lower() not in ALLOWED_METHODS:
        print('Method does not allowed')
        return

    with requests.Session() as session:
        # Hopefully server is support ranges
        session.headers.update(headers)
        session.headers['Range'] = "bytes=0-100"
        session.max_redirects = depth
        try:
            r = getattr(session, method)(url,
                                         allow_redirects=True,
                                         data=payload,
                                         stream=True)
        except TooManyRedirects:
            print(f'Too many redirects. Cant proceed with current maximum depth ({depth})')
            return

        if r.status_code in (200, 201, 202):
            print(f'The final url is {r.url}')
        else:
            print(f'Url response with status {r.status_code}')
        r.close()


if __name__ == '__main__':
    get_final_url()
