set myList {
    "00000001"
    "00000010"
    "00000100"
    "00001000"
    "00010000"
    "00100000"
    "01000000"
    "10000000"
}
# puts [lindex $myList 2]


for {set a 0} {$a < 8} {incr a} {
    puts "value of myList: [lindex $myList $a]"
}