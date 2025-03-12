# coding=utf-8

__version__ = "2.0.0"


import json
from io import BytesIO
import requests
import sys

class Client:
    """Client for interacting with the Kraken.io API."""

    def __init__(self, api_key, api_secret):
        if not api_key:
            raise ValueError("Please provide a Kraken.io API Key")
        if not api_secret:
            raise ValueError("Please provide a Kraken.io API Secret")

        self.api_key = api_key
        self.api_secret = api_secret
        self.api_base_url = "https://api.kraken.io/"
        self.api_v1_url = self.api_base_url + "v1/"
        self.auth = {"auth": {"api_key": self.api_key, "api_secret": self.api_secret}}
        self.headers = {
            "User-Agent": "Kraken-Python-Client/0.2.0 (Python/3.x; +https://github.com/krakenio/kraken-python)",
            "Content-Type": "application/json",
        }

    def url(self, image_url, params):
        """Optimize an image from a URL."""
        if not image_url:
            raise ValueError("Please provide a valid image URL for optimization")
        if not params:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_v1_url + "url"
        request_data = params.copy()
        request_data["url"] = image_url
        request_data.update(self.auth)

        response = requests.post(api_endpoint, headers=self.headers, data=json.dumps(request_data))
        return self._handle_response(response)

    def upload(self, file_path, params):
        """Upload and optimize a local image file."""
        if not file_path:
            raise ValueError("Please provide a valid file path to the image")
        if not params:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_v1_url + "upload"
        request_data = params.copy()
        request_data.update(self.auth)

        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(api_endpoint, headers={"User-Agent": self.headers["User-Agent"]}, files=files, data={"data": json.dumps(request_data)})
        return self._handle_response(response)

    def upload_bytesio(self, img, params):
        """Upload and optimize an image from a BytesIO object."""
        if not isinstance(img, BytesIO):
            raise ValueError("Please provide a valid BytesIO file-like object")
        if not params:
            raise ValueError("Please provide image optimization parameters")

        api_endpoint = self.api_v1_url + "upload"
        request_data = params.copy()
        request_data.update(self.auth)

        filename = getattr(img, "name", "image.jpg")
        files = {"file": (filename, img)}

        response = requests.post(api_endpoint, headers={"User-Agent": self.headers["User-Agent"]}, files=files, data={"data": json.dumps(request_data)}, timeout=30)
        return self._handle_response(response)

    def user_status(self):
        """Check Kraken.io user status (quota usage, plan, etc.)."""
        api_endpoint = self.api_base_url + "user_status"
        response = requests.post(api_endpoint, headers=self.headers, data=json.dumps(self.auth))
        return self._handle_response(response)

    def _handle_response(self, response):
        """Handles API response and raises errors when needed."""
        try:
            response.raise_for_status()
        except requests.HTTPError:
            try:
                error_json = response.json()
                print(f"[Kraken Error] HTTP {response.status_code}: {error_json}", file=sys.stderr)
            except ValueError:
                print(f"[Kraken Error] HTTP {response.status_code}: {response.text}", file=sys.stderr)
            raise
        return response.json()


# Example usage
if __name__ == "__main__":
    client = Client("your_api_key", "your_api_secret")

    # Optimize image from URL
    params = {"wait": True, "lossy": True}
    result = client.url("https://example.com/image.jpg", params)
    print("Optimized URL:", result.get("kraked_url"))

    # Optimize image from local file
    result = client.upload("/path/to/image.jpg", params)
    print("Optimized URL:", result.get("kraked_url"))

    # Check user status
    user_status = client.user_status()
    print("User status:", user_status)
