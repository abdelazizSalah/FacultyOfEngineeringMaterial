vlog radix_4_booth_multiplier.v
vsim Radix4BoothMultiplier
add wave subRes
add wave coderReg
add wave *


force multiplier 110
force multiplicand 010
run


force multiplicand 0110
force  multiplier 0011
run

force multiplicand 1110  
force  multiplier 0111
run


force multiplicand 1111
force  multiplier 1111
run


force multiplicand 0001
force  multiplier 0000
run

force multiplicand 01010001
force  multiplier  10100000
run


force multiplicand 0100
force  multiplier 1011
run




force multiplicand 11111111111111111111111111111010 
force  multiplier 11111111111111111111111111111001 
run

force multiplicand 11111111111111111111111111110101 
force  multiplier 11111111111111111111111111111100 
run

force multiplicand 11111111111111111111111111111111 
force  multiplier 11111111111111111111111111111100 
run
    
force multiplicand 11111111111111111111111111111010 
force  multiplier 011 
run

force multiplier 11111111111111111111111111111010 
force  multiplicand 011 
run


force multiplicand 0
force  multiplier 0
run