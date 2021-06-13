import mock

from project.spiders.fundsexplorer import FundsExplorerSpider
from project.spiders.helpers.fundsexplorer import FundsExplorerHelper


class TestFundsExplorerSpider:

    def test_parse_ranking(self, ranking):
        spider = FundsExplorerSpider()
        results = [r for r in spider.parse(ranking)]

        assert len(results) == 1
        assert results[0] == {
            'code': 'HSML11',
            'activeQuantity': '5',
            'currentPrice': '90.69',
            'dailyLiquidity': '19516.0',
            'dividend': '0.35',
            'dividendYield': '0.384235371610495',
            'dividendYieldSixMonthsAccumulated': '2.28753473160812',
            'dividendYieldSixMonthsAverage': '0.381255788601353',
            'dividendYieldThreeMonthsAccumulated': '0.811320249849727',
            'dividendYieldThreeMonthsAverage': '0.270440083283242',
            'dividendYieldTwelveMonthsAccumulated': '4.43027940409677',
            'dividendYieldTwelveMonthsAverage': '0.369189950341398',
            'liquidPatrimony': '1544629510.31',
            'patrimonyValue': '97.881464',
            'patrimonyValueByPrice': '0.9265288471778477',
            'physicalVacancy': '6.6',
            'sector': 'Shoppings'
        }

    @mock.patch('scrapy.Request')
    def test_parse_funds(self, mock, urls, funds):
        spider = FundsExplorerSpider()
        [r for r in spider.parse(funds)]

        mock.assert_called_once_with(
            urls[2], callback=FundsExplorerHelper.extract_from_fund
        )
