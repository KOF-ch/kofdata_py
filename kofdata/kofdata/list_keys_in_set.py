from requests import get
from errors import KofdataError
import constants as const

def list_keys_in_set(setname):
	
	if(isinstance(setname, basestring)):
		setname = [setname]
	
	url = const.API_BASE_URL + '/sets/details/{}'
	
	sets = dict()
	
	for s in setname:
		seturl = url.format(s)
	
		response = get(seturl)
	
		if(response.status_code == 200):
			sets[s] = response.json()['keys']
		else:
			raise KofdataError('Could not read from API (status code: {})'.format(response.status_code))
	
	return sets