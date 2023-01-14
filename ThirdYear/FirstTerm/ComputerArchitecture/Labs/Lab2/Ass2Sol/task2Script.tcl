vlog task2.v
vsim RegisterFileUsingArrayMap
add wave *
for {set a 0} {$a < 8} {incr a} {
    add wave registers[$a]
}

