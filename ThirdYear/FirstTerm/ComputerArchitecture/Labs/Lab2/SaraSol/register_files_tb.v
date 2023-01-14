module register_files_tb;

  // Parameters
    localparam T = 200;
    localparam N = 4;
  // Ports
  reg read_enable = 0;
  reg  write_enable = 0;
  reg  clk = 0;
  reg  rst = 0;
  reg [N-1:0] write_data;
  reg [2:0] read_addr;
  reg [2:0] write_addr;

  wire [N-1:0] read_data_1;
  wire [N-1:0] read_data_2;

  register_file #(N)
  register_file_array (
    .read_enable (read_enable ),
    . write_enable ( write_enable ),
    . clk ( clk ),
    . rst ( rst ),
    .read_data (read_data_1 ),
    .write_data (write_data ),
    .read_addr (read_addr ),
    .write_addr  ( write_addr)
  );

  register_file_2 #(N)
  register_file_generate (
    .read_enable (read_enable ),
    . write_enable ( write_enable ),
    . clk ( clk ),
    . rst ( rst ),
    .read_data (read_data_2),
    .write_data (write_data ),
    .read_addr (read_addr ),
    .write_addr  ( write_addr)
  );

  initial begin
    $monitor("reset = %b, read_enable = %b, write_enable = %b \n",rst,read_enable,write_enable);
    $monitor("            read_addr = %d, write_addr = %d \n",read_addr,write_addr);
    $monitor("array reg file out = %d, generate reg file out = %d \n",read_data_1,read_data_2);
    
    // both register files are reset
    rst = 1;
    #T;
    //read is enabled with a read address
    rst = 0;
    read_enable =1;
    read_addr = 0;
    #T;
    //read is disabled and write is enabled to a write address with data = 5
    read_enable =0;
    write_enable =1;
    write_addr = 0;
    write_data = 5;
    #T;
    //read is enabled to the same address
    write_enable = 0;
    read_enable = 1;
    #T;
    //read address is changed
    read_addr = 3;
    #T;
    //reading and writing to the same register
    read_addr = 5;
    write_enable =1;
    write_addr = 5;
    write_data = 9;
    #(T*2);
    
    //reading and writing to different registers
    write_addr = 2;
    #T;
    
    
    //enabling all signals
    rst = 1;
    read_enable =1;
    write_enable =1;
    #T;

    //disabling rst and write
    rst = 0;
    write_enable = 0;
    #T;

    //disabling all signals
    read_enable = 0;
    #T;
    $finish;
  end

  always
    #(T/4)   clk = !  clk ;

endmodule
