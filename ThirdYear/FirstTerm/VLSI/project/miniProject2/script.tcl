vlog boothSecondTrial.v
vsim booth
add wave *
force multiplicand2 0110
force  multiplier2 0011
run

force multiplicand2 1110  
force  multiplier2 0111
run


force multiplicand2 1111
force  multiplier2 1111
run


force multiplicand2 0001
force  multiplier2 0000
run

force multiplicand2 01010001
force  multiplier2  10100000
run


force multiplicand2 0100
force  multiplier2 1011
run




force multiplicand2 11111111111111111111111111111010 
force  multiplier2 11111111111111111111111111111001 
run

force multiplicand2 11111111111111111111111111110101 
force  multiplier2 11111111111111111111111111111100 
run

force multiplicand2 11111111111111111111111111111111 
force  multiplier2 11111111111111111111111111111100 
run

force multiplicand2 11111111111111111111111111111010 
force  multiplier2 11111111111111111111111111111001 
run


force multiplicand2 0
force  multiplier2 0
run


