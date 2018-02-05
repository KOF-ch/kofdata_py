from requests import get
from errors import KofdataError
import constants as const

def list_available_sets():
	url = const.API_BASE_URL + '/sets/'
	
	response = get(url)
	
	if(response.status_code == 200):
		return response.json()
	else:
		raise KofdataError('Could not read from API (status code: {})'.format(response.status_code))