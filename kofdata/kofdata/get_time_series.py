import pandas as pd
from helpers import ts_trim
from requests import get
from six import string_types
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from errors import KofdataError
import constants as const
from helpers import ts_to_dict

def get_time_series(keys, api_key=None, as_data_frame=False, ):
	if not isinstance(keys, string_types):
		keys = ','.join(keys)

	url = const.API_BASE_URL + '/{}/ts?mime=csv&keys={}'
	if(not api_key is None):
		url = url.format('main', keys) + '&apikey={}'.format(api_key)
	else:
		url = url.format('public', keys)

	response = get(url)
	
	if(response.status_code == 200):
		sio = StringIO(response.text)
		ts = pd.read_csv(sio, index_col='date', parse_dates=True)

		if not as_data_frame:
			ts = ts_to_dict(ts)
			
		return ts
	elif(response.status_code == 403):
		raise KofdataError('Could not authenticate. Please check your API key!')
	elif(response.status_code == 412):
		missing_keys = response.json()['message']
		raise KofdataError('The API responded with {}. Are you sure the requested series are all {}?'.format(missing_keys, 'public' if api_key is None else 'non-public'))
	#else:
		# Raise exception