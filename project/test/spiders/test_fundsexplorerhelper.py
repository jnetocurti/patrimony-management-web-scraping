from project.spiders.helpers.fundsexplorer import FundsExplorerHelper


class TestFundsExplorerHelper:

    def test_extract_from_fund(self, fund):
        results = [r for r in FundsExplorerHelper.extract_from_fund(fund)]

        assert len(results) == 1
        assert results[0] == {
            'code': 'HSML11',
            'document': '32892018000131',
            'emitted_quotas': '6750000',
            'mandate': 'Renda',
            'name': 'HSI MALLS FUNDO DE INVESTIMENTO IMOBILIÁRIO',
            'target_investor': 'Investidores em Geral'
        }
