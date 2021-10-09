#! /usr/bin/env python 


import sys 
import hdlparse.vhdl_parser as vhdl
import hdlparse.verilog_parser as vlog




def generate_Test (code , rand ):
    vlog_ex = vlog.VerilogExtractor()
    vlog_mods = vlog_ex.extract_objects_from_source(code)

 
    for i in vlog_mods :
        outputfile_name = "%s_tb.v" % i.name #testbench name is the MUV name prefixed with “_tb”
        outputfile= open(outputfile_name,'w+')
        outputfile.write("`timescale 1ns/1ps" + '\n') #The timescale is 1ns/1ps
        outputfile.write('\n'+ "module   " + i.name + "_tb;"  + '\n')
        outputfile.write('\n')

       
       #connects its input ports to variables of type reg and output ports to wires.
        for j in i.ports:
            if j.mode == "input":
                outputfile.write("  reg  " + j.data_type + " "  + j.name + "_i;" +'\n')
            elif j.mode == "output":
                outputfile.write("  wire  " + j.data_type + " "  + j.name + "_o;" + '\n')
           
        outputfile.write('\n')

        #termination testbench parameter
        outputfile.write("  parameter termination = 100 ;"  + '\n')

        if rand =="-rand":
                 outputfile.write("  parameter rand_period = 10 ;"  + '\n')

        # clock period is a parameter in the testbench module
        for j in i.ports:
             if j.name == "clock" or j.name =="clk":
                 outputfile.write("  parameter period = 10 ;"  + '\n')
                 # (the polarity of the reset is a module parameter in the testbench + reset assertion duration 
             if j.name == "reset" or j.name =="rst":
                 outputfile.write("  parameter polarity = 1 ;"  + '\n')
                 outputfile.write("  parameter rst_duration = 10 ;"  + '\n')
        outputfile.write("  "+i.name + "  MUV  ( ")
        last = len(i.ports)-1

        for j in i.ports:
            if i.ports.index(j)!=last:
                outputfile.write("."+j.name +"("+j.name )
                if j.mode == "input":
                    outputfile.write("_i)"+" , ")
                elif j.mode == "output":
                    outputfile.write("_o)"+" , ")
            else:
                outputfile.write("."+j.name +"("+j.name )
                if j.mode == "input":
                    outputfile.write("_i)")
                elif j.mode == "output":
                    outputfile.write("_o)")

        outputfile.write(" );"+'\n')
        outputfile.write('\n')

        #registers must be initialized to 0.
        outputfile.write("  initial begin"+'\n')
        for j in i.ports:
            if j.mode == "input":
                outputfile.write("      "+j.name + "_i = 0;" + '\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')

        #code to generate a clock 
        for j in i.ports: 
            if j.name == "clk" :
                outputfile.write (" always #period clk_i = ~clk_i; "+ '\n')
            elif j.name == "clock" :
                outputfile.write (" always #period clock_i = ~clock_i;" + '\n')
        outputfile.write('\n')

          #reset signal generator 
        for j in i.ports:
            if j.name == "rst":
                outputfile.write("  initial begin"+'\n')
                outputfile.write("      rst_i=polarity;" + '\n')
                outputfile.write("      #(rst_duration/2);" + '\n')
                outputfile.write("      rst_i=~polarity;" + '\n')
                outputfile.write("  end"+'\n')
                outputfile.write('\n')
            elif j.name == "reset":
                outputfile.write("  initial begin"+'\n')
                outputfile.write("      reset_i=polarity;" + '\n')
                outputfile.write("      #(reset_duration/2);" + '\n')
                outputfile.write("      reset_i=~polarity;" + '\n')
                outputfile.write("  end"+'\n')
                outputfile.write('\n')
        

        #dumbs the changes in all signals
        outputfile.write("  initial begin"+'\n')
        outputfile.write("      $dumpfile(\"" + i.name + ".vcd\");" + '\n') 
        outputfile.write("      $dumpvars;"+'\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')

        #resultant testbech must be dumped on the terminal
        outputfile.write("  initial begin"+'\n')
        outputfile.write("      $display (\"\\t\\ttime")
        for j in i.ports:
            outputfile.write(",\\t" +j.name)
            if j.mode == "input":
                outputfile.write("_i")
            elif j.mode == "output":
                outputfile.write("_o")
        outputfile.write("\");" + '\n')
        outputfile.write("      $monitor(\"%d,\\t%b,\\t%b,\\t%b,\\t%d\", $time ")
        for j in i.ports:
            outputfile.write("," +j.name)
            if j.mode == "input":
                outputfile.write("_i")
            elif j.mode == "output":
                outputfile.write("_o")
        outputfile.write(");" + '\n')
        outputfile.write("  end"+'\n')
        outputfile.write('\n')


        #simulation must be terminated after some time (a testbench parameter).
        outputfile.write("  initial #termination $finish; "+'\n')
        outputfile.write('\n')


        if rand =="-rand" :
            outputfile.write("  always begin" + '\n' +"     #rand_period \n" ) 
            for j in i.ports:
                if j.mode == "input" and j.name !="clk" and j.name !="clock" and j.name !="rst" and j.name !="reset":
                    outputfile.write("      "+j.name +"_i=$random ; \n" ) 
            outputfile.write("  end  \n" )
            outputfile.write('\n')
        else :
             outputfile.write("inital begin \n" )
             outputfile.write('\n')
             outputfile.write('\n')
             outputfile.write('\n')
             outputfile.write("end  \n" )

        outputfile.write("endmodule  \n" )



def main():
    if sys.argv[1] =="-rand":
        inputfile=open(sys.argv[2] ,"r+")
    else :
        inputfile=open(sys.argv[1] ,"r+")
    code=inputfile.read()
    generate_Test(code ,sys.argv[1])
    inputfile.close()
    print ("Testbench Created")

if __name__ == "__main__": 
    main()


  
