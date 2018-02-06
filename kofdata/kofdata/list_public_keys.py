from requests import get
from errors import KofdataError
import constants as const

def list_public_keys():
	url = const.API_BASE_URL + '/public/listkeys'
	
	response = get(url)
	
	if(response.status_code == 200):
		return response.json()
	else: 
		err = 'Could not read from API (status code: {})'.format(response.status_code)
		raise KofdataError(err)