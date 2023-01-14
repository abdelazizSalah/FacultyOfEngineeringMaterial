module generic_register #(
   parameter N = 16
) (
    clk, rst, write_data, read_data
);

input clk,rst;
input [N-1:0] write_data;
output reg [N-1:0] read_data;

reg [N-1:0] data;

always @(posedge clk,posedge rst) begin

  if(rst)
  read_data = 0;
  else 
    read_data = write_data;
end    
    

endmodule