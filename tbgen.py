#! /usr/bin/env python 


import re 
import sys 
import hdlparse.vhdl_parser as vhdl
import hdlparse.verilog_parser as vlog




def sourcefile(code , rand ):
    vlog_ex = vlog.VerilogExtractor()
    vlog_mods = vlog_ex.extract_objects_from_source(code)

 
    for i in vlog_mods :
        outputfile_name = "%s_tb.v" % i.name
        outputfile= open(outputfile_name,'w+')
        outputfile.write("`timescale 1ns/1ps" + '\n')
        outputfile.write('\n'+ "module   " + i.name + "_tb;"  + '\n')
        outputfile.write('\n')


        outputfile.write("  parameter termination = 100 ;"  + '\n')

        if rand =="-rand":
                 outputfile.write("  parameter random_period = 10 ;"  + '\n')

        for j in i.ports:
             if j.name == "clock" or j.name =="clk":
                 outputfile.write("  parameter period = 10 ;"  + '\n')
             if j.name == "reset" or j.name =="rst":
                 outputfile.write("  parameter polarity = 10 ;"  + '\n')
                 outputfile.write("  parameter rst_duration = 10 ;"  + '\n')
       
        for j in i.ports:
            if j.mode == "input":
                outputfile.write("  reg  " + j.data_type + " "  + j.name + "_i;" +'\n')
            elif j.mode == "output":
                outputfile.write("  wire  " + j.data_type + " "  + j.name + "_o;" + '\n')
           
        outputfile.write('\n')
        outputfile.write("  "+i.name + "  MUV  ( ")
        last = len(i.ports)-1

        for j in i.ports:
            if i.ports.index(j)!=last:
                outputfile.write(j.name + " , " )
            else:
                outputfile.write(j.name + " " )

        outputfile.write(" );"+'\n')
        outputfile.write('\n')
        outputfile.write("  initial begin"+'\n')
        outputfile.write("      $dumpfile(\"" + i.name + ".vcd\");" + '\n')
        outputfile.write("      $dumpvars;"+'\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')

        
        outputfile.write("  initial #termination $finish "+'\n')
        outputfile.write('\n')

        outputfile.write("  initial begin"+'\n')
        outputfile.write("      $display (\"\t\ttime ")
        for j in i.ports:
            outputfile.write(",\t" +j.name)
        outputfile.write("\");" + '\n')
        outputfile.write("      $monitor (\"\%d,\t\%b,\t\%b,\t\%b,\t%d\", $time ")
        for j in i.ports:
            outputfile.write("," +j.name)
        outputfile.write(");" + '\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')

        outputfile.write("  initial begin"+'\n')
        for j in i.ports:
            if j.mode == "input":
                outputfile.write("      "+j.name + "_i = 0;" + '\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')

        for j in i.ports: 
            if j.name == "clk" :
                outputfile.write (" always #period clk = ~clk; "+ '\n')
            elif j.name == "clock" :
                outputfile.write (" always #period clock = ~clock;" + '\n')

        outputfile.write('\n')

        for j in i.ports:
            if j.name == "rst":
                outputfile.write("  initial begin"+'\n')
                outputfile.write("      rst=1;" + '\n')
                outputfile.write("      #(rst_duration/2);" + '\n')
                outputfile.write("      rst=0;" + '\n')
                outputfile.write("  end"+'\n')
                outputfile.write('\n')
            elif j.name == "reset":
                outputfile.write("  initial begin"+'\n')
                outputfile.write("      reset=1;" + '\n')
                outputfile.write("      #(reset_duration/2);" + '\n')
                outputfile.write("      reset=0;" + '\n')
                outputfile.write("  end"+'\n')
                outputfile.write('\n')
        

        if rand =="-rand" :
            outputfile.write("  always begin" + '\n' +"     #rand_period \n" ) 
            for j in i.ports:
                if j.mode == "input" and j.name !="clk" and j.name !="clock" and j.name !="rst" and j.name !="reset":
                    outputfile.write("      "+j.name +"=$random ; \n" ) 
            outputfile.write("  end  \n" )
            outputfile.write('\n')

                    
        outputfile.write("inital begin \n" )
        outputfile.write('\n')
        outputfile.write('\n')
        outputfile.write('\n')
        outputfile.write("end  \n" )



def main():
    if sys.argv[1] =="-rand":
        inputfile=open(sys.argv[2] ,"r+")
    else :
        inputfile=open(sys.argv[1] ,"r+")
    code=inputfile.read()
    sourcefile(code ,sys.argv[1])
    inputfile.close()
    print ("Testbench Created")

if __name__ == "__main__": 
    main()


  
