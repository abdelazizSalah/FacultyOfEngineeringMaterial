module register_file #(
    parameter N =16
) (
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
//  width             N-regs
reg [N-1:0] registers [7:0];

// assign read_data = registers[read_addr];

integer i;
always @(posedge clk,posedge rst)

begin 
            if(rst)  
            begin
                for(i = 0; i<8; i =i+1) 
                begin 
                    registers[i] = 0;

                end
                read_data = 0;
            end 
            else begin
                
                if(read_enable == 1 )
                begin
                    read_data = registers[read_addr];
                end
                if(write_enable == 1)
                begin
                    registers[write_addr] = write_data;
                end       
            end

end


endmodule
