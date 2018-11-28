from requests import get
import constants as const

def get_metadata(keys, locale='en'):
	url = const.API_BASE_URL + '/metadata?key={}&locale={}'
	
	if isinstance(keys, basestring):
		keys = [keys]
	
	metadata = dict()
	for key in keys:
		key_url = url.format(key, locale)
		meta = get(key_url).json()
		metadata[key] = meta
	return metadata