#-*-coding:utf-8-*-
## try except

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tear Down...')

	def test_init(self):
		d = Dict(a='testa', b = 1)
		self.assertEqual(d.a, 'testa')
		self.assertEqual(d.b, 1)
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['name'] = 'hmm'
		self.assertEqual(d.name, 'hmm')

	def test_attr(self):
		d = Dict()
		d.name = 'hmm'
		self.assertEqual(d['name'], 'hmm')
		self.assertTrue('name' in d)

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
	
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d['empty']
	
if __name__ == '__main__':
	unittest.main()



