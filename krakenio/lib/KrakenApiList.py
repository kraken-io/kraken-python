# Settings and constants
API_KRAKEN_IO = 'https://api.kraken.io'


class KrakenApiListDefaults(object):

    def __init__(self, url, methods):
        self.url = url
        self.methods = methods


class KrakenApiList(object):

    default = KrakenApiListDefaults(
        API_KRAKEN_IO,
        {
            'url': 'v1/url',
            'upload': 'v1/upload',
            'userStatus': 'user_status'
        }
    )

    def __init__(self, url=default.url, methods=default.methods):
        for method, path in methods.items():
            setattr(self, method, url + '/' + path)

    def __str__(self):
        return str(vars(self))
