
module mux2X1 (
    in0,
    in1,
    sel,
    out
);
  input in0, in1;
  input sel;
  output out;
  reg out; 

  always @ * begin
   out = (sel) ? in1 : in0;
  end
endmodule