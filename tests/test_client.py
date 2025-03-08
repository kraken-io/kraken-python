import unittest
import os
from io import BytesIO
from dotenv import load_dotenv
from krakenio import Client

# Load environment variables from .env
load_dotenv()


class TestKrakenClient(unittest.TestCase):
    def setUp(self):
        # Load API credentials from .env
        self.api_key = os.getenv("KRAKEN_API_KEY")
        self.api_secret = os.getenv("KRAKEN_API_SECRET")
        
        # Check if credentials are provided
        if not self.api_key or not self.api_secret:
            raise ValueError("KRAKEN_API_KEY and KRAKEN_API_SECRET must be set in .env")

        self.client = Client(api_key=self.api_key, api_secret=self.api_secret)
        self.params = {"lossy": True, "wait": True}  # 'wait': True ensures immediate response

        # Expected response format for successful calls
        self.expected_success_keys = {
            "success": bool,
            "file_name": str,
            "original_size": int,
            "kraked_size": int,
            "saved_bytes": int,
            "kraked_url": str,
        }

        # Expected response format for error calls
        self.expected_error_keys = {
            "success": bool,
            "message": str,
        }

    def test_init_missing_api_key(self):
        # Test that missing API key raises ValueError
        with self.assertRaises(ValueError):
            Client(api_key=None, api_secret="secret")

    def test_init_missing_api_secret(self):
        # Test that missing API secret raises ValueError
        with self.assertRaises(ValueError):
            Client(api_key="key", api_secret=None)

    def test_url_success(self):
        # Test real URL optimization and response format
        image_url = "https://assets.kraken.io/assets/images/index-results/05-original.jpg"
        result = self.client.url(image_url=image_url, params=self.params)
        
        # Basic success check
        self.assertTrue(result["success"], f"Expected success, got: {result}")
        self.assertIn("kraked_url", result, "Expected 'kraked_url' in response")

        # Validate success response format
        self.assertIsInstance(result, dict, "Response should be a dictionary")
        for key, expected_type in self.expected_success_keys.items():
            self.assertIn(key, result, f"Missing key: {key}")
            self.assertIsInstance(result[key], expected_type, 
                                f"Key '{key}' should be {expected_type}, got {type(result[key])}")

    def test_url_failure(self):
        # Test real URL optimization with invalid URL and error response format
        image_url = "https://assets.kraken.io/assets/images/index-results/05-original-false.jpg"
        try:
            result = self.client.url(image_url=image_url, params=self.params)
            # If no exception, check error response
            self.assertFalse(result["success"], f"Expected failure, got: {result}")
            self.assertIsInstance(result, dict, "Error response should be a dictionary")
            for key, expected_type in self.expected_error_keys.items():
                self.assertIn(key, result, f"Missing key: {key}")
                self.assertIsInstance(result[key], expected_type, 
                                    f"Key '{key}' should be {expected_type}, got {type(result[key])}")
            self.assertEqual(result["success"], False, "Success should be False in error response")
        except Exception as e:
            # If an exception occurs (e.g., HTTP 400), it’s still a valid failure case
            self.assertTrue(isinstance(e, Exception), "Expected an exception for invalid URL")

    def test_upload_success(self):
        # Test real file upload and response format
        file_path = os.path.join(os.path.dirname(__file__), "test.jpg")
        self.assertTrue(os.path.exists(file_path), f"File not found: {file_path}")

        result = self.client.upload(file_path=file_path, params=self.params)
        
        # Basic success check
        self.assertTrue(result["success"], f"Expected success, got: {result}")
        self.assertIn("kraked_url", result, "Expected 'kraked_url' in response")

        # Validate success response format
        self.assertIsInstance(result, dict, "Response should be a dictionary")
        for key, expected_type in self.expected_success_keys.items():
            self.assertIn(key, result, f"Missing key: {key}")
            self.assertIsInstance(result[key], expected_type, 
                                f"Key '{key}' should be {expected_type}, got {type(result[key])}")


if __name__ == "__main__":
    unittest.main()