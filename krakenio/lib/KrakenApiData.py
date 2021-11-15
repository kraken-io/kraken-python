import json


class DataEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


class KrakenApiData(object):

    def __init__(self, kraken, options={}):
        self.auth = kraken.auth
        for k, v in options.items():
            setattr(self, k, v)

    def toJson(self):
        return json.dumps(self, cls=DataEncoder, separators=(',', ':'))
