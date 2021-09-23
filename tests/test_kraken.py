# coding=utf-8

# Standard libraries
import os
try:
    from cStringIO import StringIO as cStringIO
except ImportError:
    from io import BytesIO as cStringIO

# External libraries
import pytest

# Internal libraries
from krakenio import Client

# Constants
KEY = os.environ['KRAKEN_API_KEY']
SECRET = os.environ['KRAKEN_API_SECRET']
LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
TEST_FILE = os.path.join(LOCATION, 'support/images/image.gif')
DEV_OPTIONS = {
    'wait': True,
    'dev': True
}

# Creates kraken instance
@pytest.fixture(scope='class', autouse=True)
def kraken_instance():
    return Client(KEY, SECRET)

class TestKraken:
    """Kraken tests module
    """

    def test_construct(self):
        """Test Kraken constructor
        """
        kraken = Client(KEY, SECRET)
        assert type(kraken) is Client, 'instance creation failed'
        assert kraken.auth.api_key == KEY, 'api_key wrong value'
        assert kraken.auth.api_secret == SECRET, 'api_secret wrong value'

    def test_userStatus(self, kraken_instance):
        """Test kraken.userStatus method

        Args:
            kraken_instance (Client): kraken_instance
        """
        response = kraken_instance.userStatus()
        assert response.success, 'kraken.userStatus() failed: ' + response.error

    def test_url(self, kraken_instance):
        response = kraken_instance.url(
            'https://kraken-nekkraug.netdna-ssl.com/assets/images/kraken-logotype@2x.png',
            DEV_OPTIONS
        )
        assert response.success, 'kraken.url() failed: ' + response.message

    def test_upload_file_path(self, kraken_instance):
        """Test kraken.upload method

        Args:
            kraken_instance (Client): kraken_instance
        """
        response = kraken_instance.upload(TEST_FILE, DEV_OPTIONS)
        assert response.success, 'kraken.upload() failed: ' + response.message

    def test_upload_file_data(self, kraken_instance):
        """Test kraken.upload_stringio method

        Args:
            kraken_instance (Client): kraken_instance
        """
        file = cStringIO(open(TEST_FILE, 'rb').read())
        response = kraken_instance.upload_stringio(file, DEV_OPTIONS)
        assert response.success, 'kraken.upload_stringio() failed: ' + response.message
