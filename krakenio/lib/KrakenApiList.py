# Settings and constants
API_KRAKEN_IO = 'https://api.kraken.io'


class KrakenApiListDefaults(object):
    """Default options for KrakenApiList

    Args:
        object (object): default inheritance from object
    """
    def __init__(self, url, methods):
        self.url = url
        self.methods = methods


class KrakenApiList(object):
    """Kraken API methods URLs list

    Args:
        object (object): default inheritance from object
    """

    default = KrakenApiListDefaults(
        API_KRAKEN_IO,
        {
            'url': 'v1/url',
            'upload': 'v1/upload',
            'userStatus': 'user_status'
        }
    )
    """Default options for KrakenApiList
    """

    def __init__(self, url=None, methods=None):
        """Create new KrakenApiList instance

        Args:
            url (string, optional): Kraken API host URL. Defaults to `KrakenApiList.default.url`.
            methods (object, optional): Kraken API methods list. Defaults to `KrakenApiList.default.methods`.
        """
        url = url or KrakenApiList.default.url
        methods = methods or KrakenApiList.default.methods
        for method, path in methods.items():
            setattr(self, method, url + '/' + path)

    def __str__(self):
        return str(vars(self))
