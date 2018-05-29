import requests
import jsonpickle

from .response import TeamGridPyResponse

def verbosable(func):
	def wrapper(*args, **kwargs):
		if args[0].verbose:
			print('/'.join([args[0].api_url, args[1]]))
			print(args[0].params)
		return func(*args, **kwargs)
	return wrapper


class TeamGridPyBase():
	api_url = 'https://api.teamgridapp.com'
	def __init__(self, api_key, *args, **kwargs):
		self.session = requests.Session()
		self.session.headers.update({'Authorization': f'Bearer {api_key}'})
		self.verbose = kwargs.get('verbose', False)
		self.limit = 1000
		self.params = {}

	@property
	def params(self):
		return self.__params

	@params.setter
	def params(self, params):
		if isinstance(params, dict):
			params = dict((k,v) for k,v in params.items() if v is not None)
			self.__params = params
		else:
			raise TypeError('Params need to be of type dict!')

	@staticmethod
	def to_json(obj):
		return jsonpickle.encode(obj, unpicklable=False)

	@verbosable
	def get(self, endpoint, id_=None, all_=False):
		url = '/'.join(filter(None, [self.api_url, endpoint, id_]))
		params = self.params
		if id_:
			params = {}
		response = self.session.get(url, params=params)
		return TeamGridPyResponse(response)


			
	def create(self, endpoint, obj):
		url = '/'.join(filter(None, [self.api_url, endpoint]))
		data = self.to_json(obj)
		response = self.session.post(url, data=data)
		return self.parse_response(response)

			
	def update(self, endpoint, id_, obj):
		url = '/'.join(filter(None, [self.api_url, endpoint, id_]))
		data = self.to_json(obj)
		response = self.session.put(url, data=data)
		return self.parse_response(response)

			
			
	def delete(self, endpoint, id_):
		url = '/'.join(filter(None, [self.api_url, endpoint, id_]))
		self.session.delete(url)


if __name__ == '__main__':
	pass