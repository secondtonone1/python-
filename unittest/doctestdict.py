#-*-coding:utf-8-*-
## try except

class Dict(dict):
	'''
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2=Dict(a=1,b=2,c='m')
	>>> d2.c
	'm'
	
	'''
	def __init__(self, **kw):
		super(Dict,self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError('AttributeError key is %s' %key)
	def __setattr__(self,key,value):
		self[key] = value


if __name__ == '__main__':
	import doctest
	doctest.testmod()


