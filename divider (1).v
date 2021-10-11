`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/09/2021 02:17:23 AM
// Design Name: 
// Module Name: divider
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module divider #(parameter n = 250000)(input clk, rst, output reg clk_out);
    reg [31:0] count;
    always @ (posedge clk, posedge rst) begin // Asynchronous Reset
        if (rst == 1'b1)
            count <= 32'b0;
        else if (count == n-1)
            count <= 32'b0;
        else
            count <= count+1;
    end
    always @ (posedge clk, posedge rst) begin // Asynchronous Reset
        if (rst == 1'b1)
            clk_out <= 1'b0;
        else if (count == n-1)
            clk_out <= ~clk_out;
        else
            clk_out <= clk_out;
    end
endmodule
