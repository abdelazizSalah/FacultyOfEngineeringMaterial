
module block_norm ( ES, Co, MS, M, E); 
    ///defining inputs
    input [7:0] ES,
    input Co,
    input [27:0] MS,

    /// defining the outputs
    output [22:0] M,
    output [7:0] E

    /// defining utility wires 
    wire [4:0] Zcount_aux, shift;
    wire [27:0] number;

    /// instantiating a new object of zero counter
  zero_counter zc (
      MS,
      Zcount_aux
  );

  /// instantiating new object of the exponents
  exponent exp (
      ES,
      Co,
      Zcount_aux,
      shift,
      E
  );

  /// instantiating new object of the n_shift
  n_shift sh (
      shift,
      MS,
      number
  );
  /// instantiating new object of the round 
  round r (
      number,
      M
  );
endmodule