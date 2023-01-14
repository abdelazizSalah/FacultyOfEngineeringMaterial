module exponent (input [7:0] ES, input Co, input [4:0]Zcount_aux, output reg [4:0] shift, output reg [7:0] E) ;
always @ * begin 
   shift = (ES[4:0] > Zcount_aux[4:0]) ? Zcount_aux : (ES[4:0] < Zcount_aux) ? ES[4:0] : Zcount_aux;
   E = (ES > Zcount_aux) ? ES - shift + Co : (ES < Zcount_aux) ? 8'h00 : 8'h01;
end 
endmodule