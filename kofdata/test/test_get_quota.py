import unittest
from kofdata import get_quota
from kofdata import KofdataError

class TestGetQuota(unittest.TestCase):
	def test_invalid_api_key(self):
		with self.assertRaisesRegexp(KofdataError, 'returned a status code'):
			get_quota('notakey')
		
if __name__ == '__main__':
	unittest.main()