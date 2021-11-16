class KrakenAuth(object):
    """Kraken Auth object with key and secret

    Args:
        object (object): default inheritance from object
    """

    def __init__(self, api_key, api_secret):
        """Create new KrakenAuth instance

        Args:
            api_key (string): Kraken API key
            api_secret (string): Kraken API secret
        """
        self.api_key = api_key
        self.api_secret = api_secret
