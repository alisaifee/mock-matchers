import hamcrest
from functools import wraps
from hamcrest.core.base_matcher import BaseMatcher

__all__ = []

def _wrap(obj):
	@wraps(obj)
	def __inner(*a, **kwargs):
		resp = obj(*a, **kwargs)
		if isinstance(resp, BaseMatcher):
			meth = lambda s, o: s.matches(o)
			resp.__class__.__eq__ = meth
		return resp
	return __inner

for thing in [k for k in dir(hamcrest) if not k.startswith("_") and callable(getattr(hamcrest, k))]:
	__all__.append(thing)
	globals()[thing] = _wrap(getattr(hamcrest, thing))


