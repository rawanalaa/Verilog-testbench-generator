/*
	Digital ASIC Development, The Open Source Way
	Lab 1: Verilog Simulation
		- 8-bit signed Multiplier 
	
	Author: Mohamed Shalan
*/
module mul (
	input [7:0] mp, mc, 
	output [15:0] p 
	);

	// ump is the absolute value of mp; same for umc
	wire [7:0] ump = mp[7] ? (~mp + 1'b1) : mp;
	wire [7:0] umc = mc[7] ? (~mc + 1'b1) : mc;
	
	// up is the product resulted from multiplying the absolute values of mc and mp
	wire [15:0] up = ump * umc;

	// produce the product from up based n the signs of mp and mc
	assign p = (sign == 1'b0) ? up : (~up + 1'b1);
	wire sign = mp[7] ^ mc[7];

endmodule
