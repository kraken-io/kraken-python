# coding=utf-8

__version__ = "2.0.0"

import json
from io import BytesIO
import requests
import sys


class Client:
    """Client for interacting with the Kraken.io API."""

    def __init__(self, api_key=None, api_secret=None):
        if api_key is None:
            raise ValueError("Please provide a Kraken.io API Key")
        if api_secret is None:
            raise ValueError("Please provide a Kraken.io API Secret")

        self.api_key = api_key
        self.api_secret = api_secret
        self.api_base_url = "https://api.kraken.io/v1/"
        self.auth = {"auth": {"api_key": api_key, "api_secret": api_secret}}
        self.headers = {
            "User-Agent": "Kraken-Python-Client/2.0.0 (Python/3.x; +https://github.com/krakenio/kraken-python)",
            "Content-Type": "application/json",
        }

    def url(self, image_url=None, params=None):
        """Optimize an image from a URL."""
        if image_url is None:
            raise ValueError("Please provide a valid image URL for optimization")
        if params is None:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_base_url + "url"
        request_data = params.copy()
        request_data["url"] = image_url
        request_data.update(self.auth)

        response = requests.post(
            api_endpoint,
            headers=self.headers,
            data=json.dumps(request_data)
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            try:
                error_json = response.json()
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {error_json}",
                    file=sys.stderr
                )
            except ValueError:
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {response.text}",
                    file=sys.stderr
                )
            raise

        return response.json()

    def upload(self, file_path=None, params=None):
        """Upload and optimize a local image file."""
        if file_path is None:
            raise ValueError("Please provide a valid file path to the image")
        if params is None:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_base_url + "upload"
        request_data = params.copy()
        request_data.update(self.auth)

        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(
                api_endpoint,
                headers={"User-Agent": self.headers["User-Agent"]}, 
                files=files,
                data={"data": json.dumps(request_data)}
            )

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            try:
                error_json = response.json()
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {error_json}",
                    file=sys.stderr
                )
            except ValueError:
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {response.text}",
                    file=sys.stderr
                )
            raise

        return response.json()

    def upload_bytesio(self, img=None, params=None):
        """Upload and optimize an image from a BytesIO object."""
        if img is None or not isinstance(img, BytesIO):
            raise ValueError("Please provide a valid BytesIO file-like object")
        if params is None:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_base_url + "upload"
        request_data = params.copy()
        request_data.update(self.auth)

        filename = getattr(img, "name", "image.jpg")
        files = {"file": (filename, img)}
        
        response = requests.post(
            api_endpoint,
            headers={"User-Agent": self.headers["User-Agent"]},
            files=files,
            data={"data": json.dumps(request_data)},
            timeout=30,
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            try:
                error_json = response.json()
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {error_json}",
                    file=sys.stderr
                )
            except ValueError:
                print(
                    f"[Kraken Error] HTTP {response.status_code}: {response.text}",
                    file=sys.stderr
                )
            raise

        return response.json()


if __name__ == "__main__":
    # Example usage
    client = Client(api_key="your_api_key", api_secret="your_api_secret")
    params = {"lossy": True, "quality": 80}

    try:
        result = client.url(image_url="https://assets.kraken.io/assets/images/index-results/05-original.jpg", params=params)
        print("Result:", result)
    except requests.HTTPError as err:
        print(f"[Main Error] Caught HTTPError: {err}", file=sys.stderr)
