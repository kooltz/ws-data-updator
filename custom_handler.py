from handler import MessageHandler
import pymongo

class MongoDB:
    def __init__(self, url, database) -> None:
        self.client = pymongo.MongoClient(url)
        self.db = self.client[database]
    
    def insert(self, collection, document):
        print(f'Insert DB [{collection}]')
        # return self.db[collection].insert_one(document)


class CustomMessageHandler(MessageHandler):
    def __init__(self, mongo_db: MongoDB, identifier) -> None:
        self.mongo_db = mongo_db
        self.identifier = identifier
        self.last_updated = ''


    def process(self, message):
        try:
            key = message['data']['ResultGame']['STARTTIME']
            value = message['data']['ResultGame']['RESULT']

            if self.last_updated != key:
                self.last_updated = key
                print(f"[{self.identifier}] - [{key}] - {value}")

                return {
                    'id': self.identifier,
                    'data': message['data']['ResultGame']
                }

        except Exception as e:
            print(e)

        return None


    def post_process(self, result):
        try:
            collection = result['id']
            document = result['data']
            
            self.mongo_db.insert(collection, document)

        except Exception as e:
            print(e)
