from requests import get
from errors import KofdataError
import constants as const

def ts_trim(ts):
	ts = ts.loc[ts.first_valid_index():]
	return ts.loc[:ts.last_valid_index()]
	
def ts_to_dict(ts):
	ts = ts.to_dict(orient='series')
	return dict((k, ts_trim(v)) for k, v in ts.items())
	
def get_cdc_files(username, api_key):
	url = const.API_BASE_URL + '/user/{}/datasets?apikey={}'.format(username, api_key)
	
	listing = get(url)
	
	if(listing.status_code == 200):
		return listing.json()
	elif(listing.status_code == 403):
		raise KofdataError('Could not authenticate. Please check your API key!')
	elif(listing.status_code == 404):
		raise KofdataError('Could not find endpoint. Please check your user name!')
	#else:
		# other