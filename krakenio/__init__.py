# coding=utf-8

import cStringIO
import json
import requests


class Client(object):
    def __init__(self, api_key=None, api_secret=None):
        if api_key is None:
            raise StandardError('Please provide Kraken.io API Key')

        if api_secret is None:
            raise StandardError('Please provide Kraken.io API Secret')

        self.api_key = api_key
        self.api_secret = api_secret
        self.api_base_url = 'https://api.kraken.io/v1/'

        self.auth = {
            'auth': {
                'api_key': api_key,
                'api_secret': api_secret
            }
        }

    def url(self, image_url=None, params=None):
        if image_url is None:
            raise StandardError('Please provide a valid image URL for optimization')

        if params is None:
            raise StandardError('Please provide image optimization parameters')

        api_endpoint = self.api_base_url + 'url'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36',
            'content-type': 'application/json'
        }

        params['url'] = image_url

        params.update(self.auth)

        r = requests.post(url=api_endpoint, headers=headers, data=json.dumps(params))

        if r.ok:
            return r.json()
        else:
            details = None

            try:
                return r.json()
            except Exception as e:
                raise StandardError('Could not parse JSON response from the Kraken.io API')

    def upload(self, file_path=None, params=None):
        if file_path is None:
            raise StandardError('Please provide a valid file path to the image')

        if params is None:
            raise StandardError('Please provide image optimization parameters')

        api_endpoint = self.api_base_url + 'upload'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'
        }

        params.update(self.auth)

        files = {
            'file': open(file_path, 'rb')
        }

        r = requests.post(url=api_endpoint, headers=headers, files=files, data={
            'data': json.dumps(params)
        })

        if r.ok:
            return r.json()
        else:
            details = None

            try:
                return r.json()
            except Exception as e:
                raise StandardError('Could not parse JSON response from the Kraken.io API')

    def upload_stringio(self, img=None, params=None):
        if img is None or not isinstance(img, cStringIO.OutputType):
            raise StandardError('Please provide a valid StringIO file like object')
        if params is None:
            raise StandardError('Please provide image optimization parameters')

        api_endpoint = self.api_base_url + 'upload'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'
        }

        params.update(self.auth)

        files = {
            'file': img.getvalue()
        }

        r = requests.post(url=api_endpoint, headers=headers, files=files, data={
            'data': json.dumps(params)
        })

        if r.ok:
            return r.json()
        else:
            details = None

            try:
                return r.json()
            except Exception as e:
                raise StandardError('Could not parse JSON response from the Kraken.io API')
