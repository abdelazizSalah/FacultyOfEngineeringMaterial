module vector (
    input S,
    input [7:0] E,
    input [22:0] M,
    output reg [31:0] N
);

  always @ * begin 
   N[31] = S;
   N[30:23] = E;
   N[22:0] = M;
  end
endmodule