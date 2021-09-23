# coding=utf-8

# Standard libraries
import json
import requests
from requests import api

# Internal libraries
from .lib import KrakenAuth, KrakenApiList, KrakenApiData, KrakenResponse

# Constants and settings
USER_AGENT = 'kraken-python/0.2.0'
POST_HEADERS = {
    'User-Agent': USER_AGENT,
    'content-type': 'application/json'
}
UPLOAD_HEADERS = {
    'User-Agent': USER_AGENT
}

class Client(object):
    """Kraken.io client

    Args:
        object (object): default inheritance from object
    """

    def __init__(self, api_key, api_secret, timeout=None):
        """Create new Kraken.io client instance

        Args:
            api_key (string): Kraken.io API key string
            api_secret (string): Kraken.io API secret string
            timeout (int, optional): Requests timeout. Defaults to None.
        """
        self.auth = KrakenAuth(api_key, api_secret)
        self.api = KrakenApiList()
        self.timeout = timeout

    def post(self, url, params={}, fileData=None):
        """Send POST request to API url

        Args:
            url (string): Kraken.io API url
            params (dict, optional): Request options. Defaults to {}.
            fileData (stringIo|BufferReader, optional): File data for file request. Defaults to None.

        Returns:
            KrakenResponse: request result
        """
        krakenData = KrakenApiData(self, params).toJson()

        if fileData is None:            # Sending data
            headers = POST_HEADERS
            file=None
            data= krakenData
        else:                           # Sending file
            headers = UPLOAD_HEADERS
            file = {
                'file': fileData
            }
            data= {
                'data': krakenData
            }

        result = requests.post(         # Sending request
            url=url,
            headers=headers,
            data=data,
            timeout=self.timeout,
            files=file
        )

        return KrakenResponse(json.loads(result.text))  # Parsing result

    def url(self, image_url, params={}):
        """Krak image via URL

        Args:
            image_url ([type]): [description]
            params (dict, optional): [description]. Defaults to {}.

        Returns:
            KrakenResponse: kraked image details
        """
        params['url'] = image_url
        return self.post(self.api.url, params)

    def upload(self, file_path, params={}):
        """Upload image to Kraken.io and Krak it

        Args:
            file_path (string): full path to file
            params (dict, optional): Kraken API options. Defaults to {}.

        Returns:
            KrakenResponse: kraked image details
        """
        data = open(file_path, 'rb')
        return self.post(self.api.upload, params, data)

    def upload_stringio(self, img, params={}):
        """Upload image to Kraken.io and Krak it

        Args:
            img (StringIO|BytesIO): file data
            params (dict, optional): Kraken API options. Defaults to {}.

        Returns:
            KrakenResponse: kraked image details
        """
        data = img.getvalue()
        return self.post(self.api.upload, params, data)

    def userStatus(self):
        """Get user status

        Returns:
            KrakenResponse: user status details
        """
        return self.post(self.api.userStatus)
