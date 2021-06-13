from itemadapter import ItemAdapter

from project.mongodb import MongoDB


class RealEstateFundPipeline:

    def __init__(self):
        db = MongoDB.instance()
        self.collection = db['RealEstateFund']

    def process_item(self, item, spider):
        data = ItemAdapter.asdict(item)
        self.collection.update_one(
            {'code': data.get('code')}, {'$set': data}, True
        )

        return item
