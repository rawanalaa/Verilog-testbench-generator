#! /usr/bin/env python 


import re 
import sys 
import hdlparse.vhdl_parser as vhdl
import hdlparse.verilog_parser as vlog




def sourcefile(code):
    vlog_ex = vlog.VerilogExtractor()
    vlog_mods = vlog_ex.extract_objects_from_source(code)

 
    for i in vlog_mods :
        outputfile_name = "%s_tb.v" % i.name
        outputfile= open(outputfile_name,'w+')
        outputfile.write("`timescale 1ns/1ps" + '\n')
        outputfile.write('\n'+ "module   " + i.name + "_tb;"  + '\n')
        outputfile.write('\n')

        for j in i.ports:
            if j.mode == "input":
                outputfile.write("reg  " + j.data_type + " "  + j.name + " ;" +'\n')
            elif j.mode == "output":
                outputfile.write("wire  " + j.data_type + " "  + j.name + " ;" + '\n')

        outputfile.write('\n')
        outputfile.write(i.name + "  MUV  ( ")
        last = len(i.ports)-1

        for j in i.ports:
            if i.ports.index(j)!=last:
                outputfile.write(j.name + "  , " )
            else:
                outputfile.write(j.name + "   " )

        outputfile.write(" );"+'\n')
        outputfile.write('\n')
        outputfile.write("initial begin"+'\n')
        outputfile.write("$dumpfile(\"" + i.name + ".vcd\");" + '\n')
        outputfile.write("$dumpvars;"+'\n')
        outputfile.write("end"+'\n')
       

         
        
        

def main():
    inputfile=open(sys.argv[1] ,"r+")
    code=inputfile.read()
    sourcefile(code)
    inputfile.close()
    print ("Testbench Created")

if __name__ == "__main__": 
    main()


  
