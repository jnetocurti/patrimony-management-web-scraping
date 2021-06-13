from pymongo.database import Database

from project.mongodb import MongoDB


class TestMongoDB:

    def test_instance(self):
        instance = MongoDB.instance()
        assert instance is not None
        assert instance.name == 'mongodev'
        assert type(instance) == Database
