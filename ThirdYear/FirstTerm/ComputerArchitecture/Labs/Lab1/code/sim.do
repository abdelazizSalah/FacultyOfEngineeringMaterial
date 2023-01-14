vlog half_adder.v
vsim half_adder
add wave half_adder:x half_adder:y half_adder:s
add wave c
force half_adder:x 1
force half_adder:y 1
run
force half_adder:x 0
force half_adder:y 1
run

