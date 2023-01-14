module Adder #(
    parameter Width = 32
) (add1_i, add2_i, A_S, sum_o, carry_o);
    input [Width-1:0] add1_i;
    input [Width-1:0] add2_i;
    input A_S;
    output [Width-1:0] sum_o;
    output carry_o;
reg [Width -1 : 0]sum_o;
reg carry_o;



  always @ * begin
   {carry_o, sum_o} = (A_S == 0) ? (add1_i + add2_i) : (add1_i + {add2_i[Width-1:1], ~add2_i[0]});
  end

endmodule