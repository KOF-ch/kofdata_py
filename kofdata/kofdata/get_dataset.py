import pandas as pd
from helpers import ts_trim, ts_to_dict
from requests import get
import StringIO
from errors import KofdataError
import constants as const

def get_dataset(set_name, api_key=None, as_data_frame=False, ):
	url = const.API_BASE_URL + '/{}/sets/{}?mime=csv'
	if(not api_key is None):
		url = url.format('main', set_name) + '&apikey={}'.format(api_key)
	else:
		url = url.format('public', set_name)

	response = get(url)
	
	if(response.status_code == 200):
		sio = StringIO.StringIO(response.text)
		ts = pd.read_csv(sio, index_col='date', parse_dates=True)

		if not as_data_frame:
			ts = ts_to_dict(ts)
			
		return ts
	elif(response.status_code == 403):
		raise KofdataError('Could not authenticate. Please check your API key!')
	elif(response.status_code == 404):
		missing_keys = response.json()['message']
		raise KofdataError('The API responded with {}. Are you sure the requested set is {}?'.format(missing_keys, 'public' if api_key is None else 'non-public'))
	#else:
		# Raise general exception