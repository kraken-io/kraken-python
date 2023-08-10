import json


class DataEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class KrakenApiData(object):
    """Kraken API data object

    Args:
        object (object): default inheritance from object
    """

    def __init__(self, auth, options={}):
        """Create new KrakenApiData instance

        Args:
            auth (KrakenAuth): Kraken Auth object with key and secret
            options (dict, optional): API option. Defaults to {}.
        """
        self.auth = auth
        for k, v in options.items():
            setattr(self, k, v)

    def toJson(self):
        """Convert object to JSON string

        Returns:
            string: JSON string with all object properties
        """
        return json.dumps(self, cls=DataEncoder, separators=(',', ':'))
