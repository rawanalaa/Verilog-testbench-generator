#! /usr/bin/env python 

# <xfguo@xfguo.org> wrote a file that we used as a reference for this project .

import re 
import sys 
import hdlparse.vhdl_parser as vhdl
import hdlparse.verilog_parser as vlog
from hdlparse.vhdl_parser import VhdlComponent


class tbgen(object):


	def __init__(self, infilename): #constructor 
		self.infilename = infilename
		self.module_name = ""
		self.clock_name = 'clk'
		self.reset_name = 'rst'
		self.outputfile_name = None
		self.open_outputfile()
		self.inputfile=None
		self.outfile  = sys.stdout
		self.textinfile = ""
		self.open_inputfile()
		self.parser()
		self.open_outputfile()
		vhdl_ex = vhdl.VhdlExtractor()
		vlog_ex = vlog.VerilogExtractor()
		

	def open_inputfile (self): #read the module file 
		try:
			self.inputfile = open(self.infilename, 'r')
			self.textinfile= self.inputfile.read()
			vlog_mods = vlog_ex.extract_objects_from_source(textinfile)

		except:
			print ("input file cannot be opened")
			sys.exit(1)

	def open_outputfile (self):#create testbench file
		outputfile_name = "%s_tb.v" % self.module_name
		self.outfile = open (self.outputfile_name, 'w')

	def space_remover(self,text):
		text=re.sub(r"//[^\n^\r]*", '\n', text)
		text = re.sub(r"/\*.*\*/", '', text)
		text = re.sub(r'    +', ' ', text)





	if __name__ == "__main__": #main function 

		if len(sys.argv) == 1:
			print ("Invailed Command Use: tbgen.py input_verilog_file_name ")
			sys.exit(1)
		print("Object  NOT Created")
		testbench=tbgen(sys.argv[1])
		print("Object Created")
		#testbench.print_module_head()
		#testbench.print_wires()
		#testbench.print_dut()
		#testbench.print_clock_gen()
		#testbench.print_module_end()
		#testbench.close()