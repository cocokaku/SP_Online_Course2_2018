"""
    module that will login to mongodb
"""

import configparser
from pathlib import Path
import pymongo


config_file = Path(__file__).parent.parent / '.config/config.ini'
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')

    client = pymongo.MongoClient(f"mongodb://{user}:{pw}@cluster0-shard-00-00-ofcip.mongodb.net:27017,cluster0-shard-00-01-ofcip.mongodb.net:27017,cluster0-shard-00-02-ofcip.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")

    return client
