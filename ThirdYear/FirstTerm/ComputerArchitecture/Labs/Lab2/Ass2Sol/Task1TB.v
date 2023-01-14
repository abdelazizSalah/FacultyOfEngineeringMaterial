module task1WithForGenerateTB ;
// local params
localparam Time = 100 ;

// inputs 
reg rst, clk,rdEn,wrEn;
reg[2:0] rdAddr, wrAddr; 
reg [15:0] wrData ;

// output
wire [15:0] rdData; 

// instantiate unit under test 
regFileTask1 R1(
    .rst (rst), 
    .clk (clk), 
    .read_enable (rdEn), 
    .write_enable (wrEn), 
    .write_data (wrData), 
    .read_data (rdData) ,
    .read_addr (rdAddr), 
    .write_addr (wrAddr)
);

// initial block 
initial begin 
    $monitor("input data = %b,output Data = %b", wrData, rdData);
clk = 0; 
rst = 1; 
rdEn = 1;
wrEn= 1;
wrData = 16'b0101010101011111; 
rdAddr = 000; 
wrAddr = 000;
end
// always block for the clock
always begin 
    // toggel the clk each 50ms
    #50 clk = ~clk; 
end

always begin 
    #(Time * 10)rst = 1; 
end

always begin
    #(Time * 2) if(rst == 1)
        rst = 0 ;
end

always begin
    #Time rdEn = 0; 
    wrEn = 1; 
    wrData = wrData << 1;
    wrAddr = wrAddr + 1; 
    #Time wrEn = 0 ; 
    rdEn = 1; 
    rdAddr = rdAddr + 1; 
end


endmodule