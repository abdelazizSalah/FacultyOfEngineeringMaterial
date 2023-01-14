# ModelSim Commands
vlog encoder.v
vsim encoder
add wave * 

# TCL Code 
set myList {
    "00000000"
    "00000001"
    "00000010"
    "00000100"
    "00001000"
    "00010000"
    "00100000"
    "01000000"
    "10000000"
}

# testing enable 1 
#for {set a 0} {$a < 9} {incr a} { 
#   force en 1
#  force in 8'b[lindex $myList $a]
# run
#}


# testing enable 0
#for {set a 0} {$a < 8} {incr a} { 
 #   force en 0
  #  force in 8'b[lindex $myList $a]
   # run
#}


# all possible combinations for input
force en 1
for {set a 0} {$a < 2} {incr a} { 
    for {set b 0} {$b < 2} {incr b} { 
        for {set c 0} {$c < 2} {incr c} { 
            for {set d 0} {$d < 2} {incr d} { 
                for {set e 0} {$e < 2} {incr e} { 
                    for {set f 0} {$f < 2} {incr f} { 
                        for {set g 0} {$g < 2} {incr g} { 
                            for {set h 0} {$h < 2} {incr h} { 
                                    force in 8'b$a$b$c$d$e$f$g$h
                                    run
                                }
                            }
                        }
                    }
                }
            }
    }
}

# all possible combinations for input with en 0
force en 0
for {set a 0} {$a < 2} {incr a} { 
    for {set b 0} {$b < 2} {incr b} { 
        for {set c 0} {$c < 2} {incr c} { 
            for {set d 0} {$d < 2} {incr d} { 
                for {set e 0} {$e < 2} {incr e} { 
                    for {set f 0} {$f < 2} {incr f} { 
                        for {set g 0} {$g < 2} {incr g} { 
                            for {set h 0} {$h < 2} {incr h} { 
                                    force in 8'b$a$b$c$d$e$f$g$h
                                    run
                                }
                            }
                        }
                    }
                }
            }
    }
}
