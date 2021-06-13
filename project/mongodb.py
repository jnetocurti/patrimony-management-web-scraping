import pymongo
from scrapy.utils.project import get_project_settings


class MongoDB:
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            settings = get_project_settings()
            connection = cls._create_connection(settings)
            cls._instance = connection[settings.get('MONGO_AUTH_SOURCE')]

        return cls._instance

    @classmethod
    def _create_connection(cls, settings):
        return pymongo.MongoClient(
            settings.get('MONGO_URL'),
            username=settings.get('MONGO_USER'),
            password=settings.get('MONGO_PASSWORD'),
            authSource=settings.get('MONGO_AUTH_SOURCE')
        )
