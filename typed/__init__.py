import inspect


class ParameterTypeError(Exception):
	pass


class ReturnTypeError(Exception):
	pass


def typed(f: callable) -> callable:
	s = inspect.signature(f)
	types = list(map(lambda k:s.parameters[k].annotation,s.parameters.keys()))
	returntype = s.return_annotation
	def inner(*args):
		for pair in zip(args, types):
			if not type(pair[0]) == pair[1]:
				raise ParameterTypeError("expected argument of type {}, got {}".format(pair[1], type(pair[0])))
		result = f(*args)
		if type(result) != returntype:
			raise ReturnTypeError("expected return of type {}, got {}".format(returntype, type(result)))
		return result
	return inner


def newtyped(f: callable) -> callable:
	s = inspect.signature(f)
	def inner(*args, **kwargs):
		bound = s.bind(*args, **kwargs)
		bound.apply_defaults()
		result = f(*bound.args, **bound.kwargs)
		if type(result) != s.return_annotation:
			raise ReturnTypeError("expected return of type {}, got {}".format(s.return_annotation, type(result)))
		return result
	return inner
