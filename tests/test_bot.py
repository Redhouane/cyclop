import unittest

from bots.config import create_api
# from bots.like_retweet import sum


class TestBot(unittest.TestCase):
    def test_api_connection(self):
        """
        Test that our OAuth process works fine
        """
        api = create_api()
        self.assertIsNotNone(api.verify_credentials())


if __name__ == '__main__':
    unittest.main()
