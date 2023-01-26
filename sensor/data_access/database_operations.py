import pymongo
import pandas as pd

class DB_Operations:
    def __init__(self):
        self.dbName = "sensorDB"
        self.collectionName = "sensorCollection"
        self.username = "vijay"
        self.password = "asgfsgkeoglmvkfldj"
        self.mongodb = "mongodb+srv://{v1}:{v2}@cluster0.q06oiaw.mongodb.net/?retryWrites=true&w=majority".format(v1=self.username, v2=self.password)
        self.dbconnection = None
        self.client = None
        self.collectionConnection = None
        self.client = pymongo.MongoClient(self.mongodb)
        self.dbconnection = self.client[self.dbName]
        self.collectionConnection = self.dbconnection[self.collectionName]

    def load_data(self):
        try:
            data = pd.read_csv("training_dataset/aps_failure_training_set.csv")
            self.collectionConnection.insert_many(data.to_dict(orient='record'))
        except Exception as e:
            raise Exception(e)

    def read_data(self):
        try:
            data = pd.DataFrame(list(self.collectionConnection.find()))
            data.drop('_id', axis=1, inplace=True)
            data.to_csv("sensor/data_access/training_data.csv", index=False)
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    dbops = DB_Operations()

    dbops.load_data()
    dbops.read_data()