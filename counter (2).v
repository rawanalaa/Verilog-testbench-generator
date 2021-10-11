module counter #(parameter n=3)(input upDown , Inc,clk , reset , output reg [n-1:0] count);
always @(posedge clk, posedge reset) begin
 if (reset == 1)begin 
 count <= 3'd0; // non blocking assignment
 end
 else begin
    if (upDown ==0 ) begin 
            if(Inc==0)begin 
                    count <= count + 1; 
                     end
            else begin
                    count <= count + 2;
                      end
    end
    else begin 
        if(Inc==0)begin 
                count <= count - 1; 
        end
        else begin
                count <= count - 2;
        end
    end
end
end
endmodule

