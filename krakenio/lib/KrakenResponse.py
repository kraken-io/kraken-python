class KrakenResponse(object):

    def __init__(self, data):
        for k, v in data.items():
            setattr(self, k, v)

    def get(self, attr):
        return getattr(self, attr)
