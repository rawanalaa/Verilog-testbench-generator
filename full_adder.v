/*******************************************************************
*
* Module: full_adder.v
* Project: Lab_1
* Author: Mariam Dahab mhdahab@aucegypt.edu
*
* < Full Adder >
*
**********************************************************************/
module full_adder (a,b,c_in,c_out,sum);
  input a;
  input b;
  input c_in ; 
  output sum ; 
  output c_out ; 
  
//addition
  assign sum = (a ^ b) ^ c_in;
  assign c_out = (a&b) | (a&c_in) | (b&c_in);
 
  
endmodule