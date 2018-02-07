from requests import get
from errors import KofdataError
import constants as const

def translate_legacy_keys(legacy_keys, chunk_size = 100):
	
	if(isinstance(legacy_keys, basestring)):
		legacy_keys = [legacy_keys]
	
	url = const.API_BASE_URL + '/metadata/translatelegacykeys'
	
	n_keys = len(legacy_keys)
	
	start = 0
	
	translated = dict()
	
	while(start <= n_keys):
		keys = ','.join(legacy_keys[start:(start+chunk_size)])
		
		response = get(url, {'keys': keys})
		
		if(response.status_code == 200):
			translated.update(response.json())
		else:
			err = 'Could not read API (status code: {})'.format(response.status_code)
			
		start += chunk_size
		
	return translated