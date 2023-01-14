module register_file_2 
#(
    parameter N = 16
) 
(
    read_enable,
    write_enable,
    read_data,
    write_data,
    clk,
    rst,
    read_addr,
    write_addr
);
    
input read_enable, write_enable, clk, rst;
output reg [N-1:0] read_data;
input  [N-1:0] write_data;
input  [2:0] read_addr;
input  [2:0] write_addr;

//  width                   N-regs
wire [N-1:0] read_registers [7:0];
reg [N-1:0] write_registers [7:0];

genvar j;
generate
    for (j = 0; j < 8; j = j+1)
    begin
    generic_register #(N) r (
        .clk (clk),
        .rst (rst),
        .write_data (write_registers[j]),
        .read_data  (read_registers[j])
        );
    end
endgenerate
   

integer i;

always @(*)
begin
    if(rst)
        begin
            for(i =0 ; i<8; i = i+1)
            write_registers[i] =0;
        end
    else begin
        
        if(write_enable == 1)
        begin
            write_registers[write_addr] = write_data;
        end
        
    end
end

always @(posedge clk, posedge rst) begin
    
    if(rst) begin 
        read_data = 0;
    end
    else begin
        if(read_enable == 1)
        begin
            read_data = read_registers[read_addr];
        end        
    end
end

endmodule