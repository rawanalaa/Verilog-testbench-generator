#Testbench Skeleton Generator 

How to use this tool : 

  Along with downloading the python code-named "tbgen.py", you should create a Verilog file that includes an HDL code. Make sure to store the (.py) file and the (.v) file in the same directory.
  
How to run the code : 

  First, open the command terminal and make sure it is allocated to the same directory as the one that has the code and the Verilog file.
  Next, type the command :python tbgen.py verilog_file_name.v (Replace "verilog_file_name.v" with your verilog file name )
  
  Optionally, if you want to create the testbench skeleton that will generate a random value to all registers one register at a time every fixed amount of time add "-rand" before the Verilog file name in the command line.
  Finally, a Verilog file will be created, in the same directory, that will contain the testbench skeleton.
  
 Code Structure : 
    
    The first part in the main function checks if the first argument after the python file name is "-rand" or the file name. 
    Based on the result, the code will extract the file name, opens it, and read it. 
    
    Next, a function called "generate_Test" is called (where all the analysis occurs). 
    The function starts by extracting and classifying all the data in the Verilog file. This happens using the help of the function 
    VerilogExtractor, which is a built-in function, is the Verilog library in the Hdl Parse package.
    
    After that the code is divided into sections based on the order of appearance in the testbench :
    
    1- Defining the time scale of this module, which is  1ns/1ps.
    
    2- Extracting the module name to create an output file with the same name and the prefix "_tb"
    (also to write the header of the testbench module )
    
    3- Creating variables of type reg and wires (the same number as the MUV) and later connecting the MUV's input ports to the regs and output ports to wires. Also in case of having parameters in the MUV, they will be initialized before connecting the ports 
    
    4-Creating parameters: essential, such as termination time, and based on modules, such as clock period and random period. 
    
    5- Initializing all registers by zero.
    
    6- Generating clock and reset signal (in cause MUV is sequential)
    
    7- Dumbing all changes in all signals in a file named after the testbench name (.vcd extension)
    
    8- Dumbing testbench in terminal 
    
    9- Terminating stimulation after assigned time.
    
    Finally, in case the rand command was called the code will generate an always block to assign the random number for each register.
    Else, the code will open an initial block for the user to write their own testbench. 
  

  
  Testing :
  
  You can find five modules and a table explaining each testbench coverage of the features, mentioned above, in the files list. These modules can be used in testing the code and generating test benches
