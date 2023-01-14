module regFileTask1 #(parameter noOfSelectors = 3, RegSize = 16)
 	(rst, write_enable,read_enable,  write_data,read_data, read_addr,write_addr, clk);

// defining the inputs 
input  read_enable,write_enable,rst,clk;  // here I assumed that all can have the same enable wire and depending on the value of the selector I will choose which to have the operation
input [noOfSelectors - 1:0] read_addr, write_addr; /// they are the selectors of which to be read from or write into
input [RegSize - 1:0] write_data; // this is the input to the whole file 

// defining the output regs 
output reg [RegSize - 1:0] read_data;  // this is the output of the whole file 

// defining utility regs 
reg   selectors [0:7]; // this  will be like the selector of the mux, depending on its value i will enable certain register
wire [RegSize - 1: 0] dataOut[7:0]; 
reg [RegSize - 1: 0] dataIn[7:0]; 

// generating the inside registers
genvar generateLoopCntr; 
generate
for(generateLoopCntr= 0 ; generateLoopCntr< 8; generateLoopCntr= generateLoopCntr+ 1)
/// zawed el register.
 register r (.dataIn (dataIn[generateLoopCntr]) , .dataOut (dataOut[generateLoopCntr]), .enable(selectors[generateLoopCntr]), .write_enable (write_enable), .rst (rst)); 
endgenerate



// ana hena msh el mfrod enna n3ml clock ehna el mfrod nehtghl 3la ay change by7sl 34an 3la asaso a2dr ashof eh el 7sl w el clock hya gowa el register bs
// fa msh el mfrod enny a3ml etnen registers wra ba3d w hwa da el by7sl hena .
integer i;
// applying the logic depending on the read_addrector
always @(posedge clk) begin
    /// always reset all  the selectors
    for( i = 0 ; i < 8 ; i = i + 1) begin 
        selectors[i] = 1'b0;
    end

    if (rst == 1) begin 
	/// raise all the selectors 
        for( i = 0 ; i < 8; i= i + 1 ) begin 
            selectors[i] = 1'b1 ;
        end
    end else if(write_enable == 0 && read_enable == 1 )  begin // if the read_enable is high then we want to read from this file
        read_data = dataOut[read_addr];  
    end else if (write_enable == 1 && read_enable == 0) begin  // if the write enable is high then we want to write into the file
        dataIn[write_addr] = write_data;  
        selectors[write_addr] = 1'b1;
    end else if (write_enable == 1 && read_enable ==1 ) begin 
	// it will not matter in the code whether they have the same address or not as I am working blocking statements so I will always read first then write after that
            // then we should read first 
            read_data[read_addr] = dataOut[read_addr]; 
            // then we should write 
            dataIn[write_addr] = write_data; 
            selectors[write_data] = 1; 
         /// there is only one remaining case if 0 0 then nothing should happen
    end 
end
endmodule 