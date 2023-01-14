vlog booth32Seq.v
vsim both
add wave *

# here we must define the clk as a clock signal
force -freeze sim:/both/clk 1 0, 0 {50 ps} -r 100

# first we must initialize the registers
force reset 1 
run 

# then we must load the values.
force reset 0
force load 1
force Q 0110  
force M 1000
# force Q 11111111111111111111111111100000  
# force M 11111111111111111111111111111010
run
run

#now we must down the load signal
force load 0
run



# then we must run the simulation
for {set i 0} {$i < 200} {incr i} {
    run
}