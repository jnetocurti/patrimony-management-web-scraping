from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from project.items import RealEstateFund
from project.utils.processors import (
    format_as_number, replace_invalid_chars, replace_non_numeric_chars,
)

FROM_RANKING_TEXT_XPATH = 'td[{}]//text()'
FROM_RANKING_DATA_ORDER_XPATH = 'td[{}]/@data-order'

FROM_FUND_TICKER_XPATH = '//*[@id="head"]//h1/text()'
FROM_FUND_DEFAULT_XPATH = '(//span[contains(@class,"description")]/text())[{}]'  # noqa


class FundsExplorerHelper:

    @staticmethod
    def extract_from_ranking(page):
        loader = ItemLoader(
            item=RealEstateFund(), selector=page
        )
        loader.default_output_processor = TakeFirst()
        loader.default_input_processor = MapCompose(replace_invalid_chars)

        loader.add_xpath(
            'code',
            FROM_RANKING_TEXT_XPATH.format(1)
        )
        loader.add_xpath(
            'sector',
            FROM_RANKING_TEXT_XPATH.format(2)
        )
        loader.add_xpath(
            'currentPrice',
            FROM_RANKING_DATA_ORDER_XPATH.format(3)
        )
        loader.add_xpath(
            'dailyLiquidity',
            FROM_RANKING_DATA_ORDER_XPATH.format(4)
        )
        loader.add_xpath(
            'dividend',
            FROM_RANKING_DATA_ORDER_XPATH.format(5)
        )
        loader.add_xpath(
            'dividendYield',
            FROM_RANKING_DATA_ORDER_XPATH.format(6)
        )
        loader.add_xpath(
            'dividendYieldThreeMonthsAccumulated',
            FROM_RANKING_DATA_ORDER_XPATH.format(7)
        )
        loader.add_xpath(
            'dividendYieldSixMonthsAccumulated',
            FROM_RANKING_DATA_ORDER_XPATH.format(8)
        )
        loader.add_xpath(
            'dividendYieldTwelveMonthsAccumulated',
            FROM_RANKING_DATA_ORDER_XPATH.format(9)
        )
        loader.add_xpath(
            'dividendYieldThreeMonthsAverage',
            FROM_RANKING_DATA_ORDER_XPATH.format(10)
        )
        loader.add_xpath(
            'dividendYieldSixMonthsAverage',
            FROM_RANKING_DATA_ORDER_XPATH.format(11)
        )
        loader.add_xpath(
            'dividendYieldTwelveMonthsAverage',
            FROM_RANKING_DATA_ORDER_XPATH.format(12)
        )
        loader.add_xpath(
            'liquidPatrimony',
            FROM_RANKING_DATA_ORDER_XPATH.format(17)
        )
        loader.add_xpath(
            'patrimonyValue',
            FROM_RANKING_DATA_ORDER_XPATH.format(18)
        )
        loader.add_xpath(
            'patrimonyValueByPrice',
            FROM_RANKING_DATA_ORDER_XPATH.format(19)
        )
        loader.add_xpath(
            'dividendYieldPatrimonyValue',
            FROM_RANKING_DATA_ORDER_XPATH.format(20)
        )
        loader.add_xpath(
            'physicalVacancy',
            FROM_RANKING_DATA_ORDER_XPATH.format(24)
        )
        loader.add_xpath(
            'financialVacancy',
            FROM_RANKING_DATA_ORDER_XPATH.format(25)
        )
        loader.add_xpath(
            'activeQuantity',
            FROM_RANKING_DATA_ORDER_XPATH.format(26)
        )
        return loader.load_item()

    @staticmethod
    def extract_from_fund(page):
        loader = ItemLoader(
            item=RealEstateFund(), selector=page
        )
        loader.default_output_processor = TakeFirst()
        loader.default_input_processor = MapCompose(replace_invalid_chars)

        loader.add_xpath(
            'code',
            FROM_FUND_TICKER_XPATH
        )
        loader.add_xpath(
            'name',
            FROM_FUND_DEFAULT_XPATH.format(1)
        )
        loader.add_xpath(
            'document',
            FROM_FUND_DEFAULT_XPATH.format(9),
            MapCompose(replace_non_numeric_chars)
        )
        loader.add_xpath(
            'target_investor',
            FROM_FUND_DEFAULT_XPATH.format(10)
        )
        loader.add_xpath(
            'emitted_quotas',
            FROM_FUND_DEFAULT_XPATH.format(3),
            MapCompose(format_as_number)
        )
        loader.add_xpath(
            'mandate',
            FROM_FUND_DEFAULT_XPATH.format(11)
        )
        yield loader.load_item()
