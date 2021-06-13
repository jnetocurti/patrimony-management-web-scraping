import scrapy

from project.spiders.helpers.extractors import (
    extract_from_fund, extract_from_ranking,
)


class FundsExplorerSpider(scrapy.Spider):
    name = 'fundsexplorer'
    allowed_domains = ['fundsexplorer.com.br']

    start_urls = [
        'https://www.fundsexplorer.com.br/funds',
        'https://www.fundsexplorer.com.br/ranking'
    ]

    def parse(self, response):
        if response.url.endswith('ranking'):
            rows = response.xpath('//*[@id="table-ranking"]/tbody//tr')

            for row in rows:
                yield extract_from_ranking(row)

        elif response.url.endswith('funds'):
            links = response.xpath('//*[@id="fiis-list-container"]//a/@href')

            for link in links:
                yield scrapy.Request(
                    response.urljoin(link.get()),
                    callback=self.parse_callback
                )

    def parse_callback(self, response):
        yield extract_from_fund(response)
