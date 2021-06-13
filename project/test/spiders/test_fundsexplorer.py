from project.spiders.fundsexplorer import FundsExplorerSpider
from project.test.spiders.conftest import URLS


class TestFundsExplorerSpider:

    def test_parse_ranking(self, resource_get):
        spider = FundsExplorerSpider()
        results = [r for r in spider.parse(resource_get(URLS.RANKING.value))]

        assert (
            next(filter(lambda e: e['code'] == 'HSML11', results)) == {
                'activeQuantity': '5',
                'code': 'HSML11',
                'currentPrice': '90.97',
                'dailyLiquidity': '35262.0',
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
                'patrimonyValueByPrice': '0.9293894500801501',
                'physicalVacancy': '6.6',
                'sector': 'Shoppings'
            }
        )

    def test_parse_funds(self, resource_get):
        spider = FundsExplorerSpider()
        results = [r for r in spider.parse(resource_get(URLS.FUNDS.value))]

        assert (
            next(filter(lambda e: e.url.endswith('hsml11'), results)).url ==
            URLS.HSML11.value
        )

    def test_parse_fund(self, resource_get):
        spider = FundsExplorerSpider()
        results = [r for r in spider.parse_callback(
            resource_get(URLS.HSML11.value))]

        assert len(results) == 1
        assert results[0] == {
            'code': 'HSML11',
            'document': '32892018000131',
            'emittedQuotas': '6750000',
            'mandate': 'Renda',
            'name': 'HSI MALLS FUNDO DE INVESTIMENTO IMOBILIÁRIO',
            'targetInvestor': 'Investidores em Geral'
        }
