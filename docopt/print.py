#-*-coding:utf-8-*-

# coding: utf-8

""" 
Usage:
	docopttest.py [-vqrh] [FILE] ...

Arguments:
	FILE	optional input file
	
Options:
	-h --help	show this
	-v 			verbose mode
	-q			quite mode
	-r			make report

Examples:
	docoptest.py -r test.txt
"""
from docopt import docopt
if __name__ == '__main__':
	arguments = docopt(__doc__)
	print(arguments)
	


