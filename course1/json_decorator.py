import json
from functools import wraps


def to_json(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return json.dumps(result)
	return wrapper

@to_json	
def get_data(a, b):
	return [a, b]
print(get_data(25, 15))