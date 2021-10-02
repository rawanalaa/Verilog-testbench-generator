#! /usr/bin/env python 

import re 
import sys 

class tbg (object):
	def __init__(self, infilename): #define variables and class function 
		self.infilename = infilename
		self.module_name = ""
		self.clock_name = 'clk'
		self.reset_name = 'rst'
		self.outputfile_name = None
		self.open_inputfile()
		self.parser()
		self.open_outputfile()
		self.inputfile=None
		self.outfile  = sys.stdout
		self.textinfile = ""

	def open_inputfile (self):
		try:
			self.inputfile = open(self.infilename, 'r')
			self.textinfile= self.inputfile.read()
		except:
			print ("input file cannot be opened")
			sys.exit(1)

	def open_outputfile (self):
		outputfile_name = "%s_tb.v" % self.module_name
		self.outfile = open (self.outputfile_name, 'w')
		

