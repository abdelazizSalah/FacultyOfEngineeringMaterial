vlog seqRadix4Booth.v
vsim Radix4BoothMultiplierSeq
add wave *
add wave coderReg
add wave subRes
# defining the clk as clock signal. 
force -freeze sim:/Radix4BoothMultiplierSeq/clk 1 0, 0 {50 ps} -r 100

# raise the reset signal
force rst 1 
run 
force rst 0

# raise the load signal 
force load 1
force multiplier 11111100
force multiplicand 1111101111
run
run

# apply the logic for 48 cycles 
force load 0
for {set i 0} {$i < 50} {incr i} {
    run
}