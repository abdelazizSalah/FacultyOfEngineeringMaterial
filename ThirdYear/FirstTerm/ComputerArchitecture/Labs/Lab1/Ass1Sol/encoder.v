module encoder (en, in , out); 
// declarations 
input en ;
input [7:0]in ;
output [2:0] out ; 
wire [2:0] out; 
// assignments 
assign out = (en == 1'b1) ? 
(
(in == 8'b00000001) ? 3'b000:
(in == 8'b00000010) ? 3'b001:
(in == 8'b00000100) ? 3'b010:
(in == 8'b00001000) ? 3'b011:
(in == 8'b00010000) ? 3'b100:
(in == 8'b00100000) ? 3'b101:
(in == 8'b01000000) ? 3'b110:
(in == 8'b10000000) ? 3'b111:
/// if the user enters 00000000 i will output highImpedence
 3'bzzz
): 3'bzzz; /// High impedence in case of 0 enable
endmodule 