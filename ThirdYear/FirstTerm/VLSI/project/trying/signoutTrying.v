module signout (
    SA,
    SB,
    Comp,
    A,
    B,
    A_S,
    Aa,
    Bb,
    AS,
    SO
);

/// defining the inputs 
  input SA, SB, Comp, A_S;
  input [27:0] A, B;

/// defining the outputs  
  output [27:0] Aa, Bb;
  output AS, SO;
  reg SO, Aa, Bb,AS; 

  /// defining utility wires 
  reg SB_aux;
  reg [27:0] Aa_aux, Bb_aux;

  /// applying the logic for the module 
    always @ * begin
   SB_aux = SB ^ A_S;
   if(Comp) begin 
    SO = SA ;
    Aa_aux = A; 
    Bb_aux = B;
   end else begin 
    SO = SB_aux ;
    Aa_aux = B; 
    Bb_aux = A;
   end
   Aa = (SA ^ SB_aux == 1'b0) ? Aa_aux : (SA == 1'b1 && SB_aux == 1'b0) ? Bb_aux : Aa_aux;
   Bb = (SA ^ SB_aux == 1'b0) ? Bb_aux : (SA == 1'b1 && SB_aux == 1'b0) ? Aa_aux : Bb_aux;
   AS = (SA != SB_aux) ? 1'b1 : 1'b0;
    end

endmodule