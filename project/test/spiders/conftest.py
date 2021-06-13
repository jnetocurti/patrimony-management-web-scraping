import os

import pytest
from scrapy.http import HtmlResponse, Request


def get_html_response(file, url):
    file_path = os.path.join(
        os.path.dirname(__file__), f'html/{file}'
    )
    return HtmlResponse(
        url=url,
        request=Request(url=url),
        body=open(file_path, 'r').read(),
        encoding="UTF-8"
    )


@pytest.fixture
def urls():
    return [
        'https://www.fundsexplorer.com.br/ranking',
        'https://www.fundsexplorer.com.br/funds',
        'https://www.fundsexplorer.com.br/funds/hsml11'
    ]


@pytest.fixture
def ranking(urls):
    return get_html_response('ranking.html', urls[0])


@pytest.fixture
def funds(urls):
    return get_html_response('funds.html', urls[1])


@pytest.fixture
def fund(urls):
    return get_html_response('fund.html', urls[2])
