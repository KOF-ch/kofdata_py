import unittest
from kofdata import get_metadata
from kofdata import KofdataError

class TestGetMetadata(unittest.TestCase):
	
	keys_to_check = ['ch.kof.bau.run1.ng08.f12.q_cb_restrict_none.ans_count.d11',
                              'ch.kof.bau.run1.ng08.f12.q_cb_restrict_none.ans_count.d12',
                              'ch.kof.bau.run1.ng08.f12.q_cb_restrict_none.ans_count']
							  
	def test_metadata_type(self):
		md = get_metadata(self.keys_to_check[0])
		self.assertTrue(type(md) is dict)
		
	def test_no_metadata(self):
		md = get_metadata('bla')
		self.assertEqual(md['bla'].keys()[0], 'info')
		
		mdJp = get_metadata(self.keys_to_check[0], locale='jp')
		self.assertEqual(mdJp[self.keys_to_check[0]].keys()[0], 'info')
		
	def test_metadata(self):
		md = get_metadata(self.keys_to_check)
		
		self.assertEqual(md.keys(), self.keys_to_check)
		
if __name__ == '__main__':
	unittest.main()