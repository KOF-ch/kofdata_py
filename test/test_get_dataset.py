import unittest
from kofdata import get_dataset
from kofdata import KofdataError
import pandas

class TestGetDataset(unittest.TestCase):
	
	key_to_check = 'baro_vintages_monthly'

	def test_set(self):
		ts_dict = get_dataset(self.key_to_check)
				
		self.assertTrue(type(ts_dict) is dict)
		
		self.assertRegexpMatches(ts_dict.keys()[0], 'baro_[0-9]{4}m[01][0-9]')
		
		self.assertTrue(type(ts_dict[ts_dict.keys()[0]]) is pandas.core.series.Series)
		
	def test_nonexistent_key(self):
		with self.assertRaisesRegexp(KofdataError, 'The API responded'):
			get_dataset('nonexistend_key')

	def test_invalid_api_key(self):
		with self.assertRaisesRegexp(KofdataError, 'Could not authenticate'):
			get_dataset('doesntmatter', 'notakey')
		
if __name__ == '__main__':
	unittest.main()