import scrapy

from project.spiders.helpers.fundsexplorer import FundsExplorerHelper


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
                yield FundsExplorerHelper.extract_from_ranking(row)

        elif response.url.endswith('funds'):
            links = response.xpath('//*[@id="fiis-list-container"]//a/@href')

            for link in links:
                yield scrapy.Request(
                    response.urljoin(link.get()),
                    callback=FundsExplorerHelper.extract_from_fund
                )
