import unittest
from kofdata import get_time_series
from kofdata import KofdataError
import pandas

class TestGetTimeSeries(unittest.TestCase):
	
	keys_to_check = ['kofbarometer', 'ch.kof.globidx.v2017.index.che']

	def test_dict(self):
		ts_dict = get_time_series(self.keys_to_check[0])
				
		self.assertTrue(type(ts_dict) is dict)
		
		self.assertEqual(ts_dict.keys()[0], self.keys_to_check[0])
		
		self.assertTrue(type(ts_dict[self.keys_to_check[0]]) is pandas.core.series.Series)
		
	def test_df(self):
		ts_df = get_time_series(self.keys_to_check[0], as_data_frame = True)
		
		self.assertTrue(type(ts_df) is pandas.core.frame.DataFrame)
		
		self.assertEqual(ts_df.columns[0], self.keys_to_check[0])

	def test_multiple_keys(self):
		ts = get_time_series(self.keys_to_check)
		
		self.assertEqual(len(ts), 2)
		
	def test_nonexistent_key(self):
		with self.assertRaisesRegexp(KofdataError, 'The API responded'):
			get_time_series('nonexistend_key')

	def test_invalid_api_key(self):
		with self.assertRaisesRegexp(KofdataError, 'Could not authenticate'):
			get_time_series('doesntmatter', 'notakey')
		
if __name__ == '__main__':
	unittest.main()