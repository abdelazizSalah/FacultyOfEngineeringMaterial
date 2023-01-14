module RegisterFileUsingArrayMap #(parameter noOfSelectors = 3, noOfBits = 16)
             (read_enable, write_enable, clk, rst, read_data,write_data,read_addr, write_addr) ; 

// defining the variables 
input read_enable, write_enable, clk, rst;
input [noOfBits - 1:0] write_data ;
input [noOfSelectors - 1:0] read_addr, write_addr; 
output reg [15:0] read_data; 

// creating the 2D memory
reg [noOfBits - 1 : 0] registers [7:0]; /// defining array of N bits Registers.

integer i = 0 ; 
always @ (posedge clk) begin  /// always begin here

   /// reset all registers if the rst flag is high
   if(rst == 1) begin 
        for ( i = 0 ; i < 8 ; i = i + 1 ) begin
            registers[i] = 0 ;
        end
   /// writing into a register depending on which address is choosen
   end else if (write_enable == 1 && read_enable == 0) begin 

    registers[write_addr] =write_data; 

   /// reading from a register depending on which address is choosen
   end else if (write_enable == 0 && read_enable == 1) begin 
    read_data = registers[read_addr];
   end else if (write_enable == 1 && read_enable ==1) begin 
    // it will not matter in the code whether they have the same address or
    // not as I am working blocking statements so I will always read first then write after that
          
        // read first
        read_data = registers[read_addr];
        
        // then write 
        registers[write_addr] = write_data;

   end /// there is only one remaining case if 0 0 then nothing should happen
  
end /// always ends here
endmodule 


