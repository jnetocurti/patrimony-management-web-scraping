import pathlib
from enum import Enum

import betamax
import pytest
from betamax.fixtures.pytest import _betamax_recorder
from scrapy.http import HtmlResponse

cassette_dir = pathlib.Path(__file__).parent / 'fixture' / 'cassettes'
cassette_dir.mkdir(parents=True, exist_ok=True)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = cassette_dir.resolve()
    config.preserve_exact_body_bytes = True


@pytest.fixture
def betamax_recorder(request):
    return _betamax_recorder(request, parametrized=True)


@pytest.fixture
def resource_get(betamax_session):
    def get(url, *args, **kwargs):
        request = kwargs.pop('request', None)
        resp = betamax_session.get(url, *args, **kwargs)
        selector = HtmlResponse(body=resp.content, url=url, request=request)
        return selector
    return get


class URLS(Enum):
    RANKING = 'https://www.fundsexplorer.com.br/ranking'
    FUNDS = 'https://www.fundsexplorer.com.br/funds'
    HSML11 = 'https://www.fundsexplorer.com.br/funds/hsml11'
