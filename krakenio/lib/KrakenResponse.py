class KrakenResponse(object):
    """Kraken API response object

    Args:
        object (object): default inheritance from object
    """

    def __init__(self, data):
        """Create new KrakenResponse instance

        Args:
            data (object): API options
        """
        for k, v in data.items():
            setattr(self, k, v)

    def get(self, name):
        """Get KrakenResponse object property by name

        Args:
            name (string): Property name

        Returns:
            any: Property value
        """
        return getattr(self, name)
