module register #(parameter noOfBits  = 16)
                       (dataIn, dataOut, enable, write_enable, rst) ;
/// defining inputs 
input enable,write_enable, rst; 
input wire [noOfBits - 1 : 0] dataIn; 

// defining outputs 
output reg [noOfBits - 1 : 0]dataOut ;

// utility reg
reg [noOfBits - 1 : 0] ownReg;


// to make always the register giving its own value out
assign dataOut = ownReg; 

// applying the logic 
always @(posedge clk) begin
	/// we should better work on the negative edge of the rst but for simplicity i will enough with the posedge of the clk
    if(rst == 1 && enable == 1) begin
        ownReg = 0 ; 
    end
       else if(write_enable == 1 && enable == 1) begin 
            ownReg = dataIn; 
        end else begin 
	/// empty to cover other cases
	end

end

endmodule