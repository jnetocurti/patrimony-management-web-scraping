import mock

from project.pipelines import RealEstateFundPipeline
from project.spiders.fundsexplorer import FundsExplorerSpider


class TestRealEstateFundPipeline:

    @mock.patch('project.mongodb.MongoDB.instance')
    def test_process_item(self, instance, mongodb):
        instance.return_value = mongodb

        RealEstateFundPipeline().process_item(
            {'code': 'HSML11'}, FundsExplorerSpider
        )

        assert mongodb.RealEstateFund.count_documents({}) == 1
        assert mongodb.RealEstateFund.find()[0]['code'] == 'HSML11'
