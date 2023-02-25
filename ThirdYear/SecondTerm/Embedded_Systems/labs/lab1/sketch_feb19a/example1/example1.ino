// @author Abdelaziz Salah
// this is the first example 

// importing libraries 
#include <avr/io.h>
#include <util/delay.h> 
void setup() {
// Q/ configure the MC with internal 16MHZ Clock -> built in clock rate.
// A/ This is the internal default frequency of the clock.
// Configure pin 0 in PORTD as output pin
DDRD = 0x01; // 00000001
// The Led is connected to pin 0 in PORTD
PORTD = 0x01; // 1 because we work negative logic. 
// Connect the lead using negative logc to flash every 1 second
// Hardware task, connect the resistor to VCC and to the long leg of the led,
// and the short leg connect it to pin 0 on the arduino
}

void loop() { // infinite loop 
  // turn the led on 
  PORTD = 0x00; 
  PORTD = PORTD & (~(1<<PD0)); // ! ~ ->! -> 1 BIT -> 0, 1, 01101 ,00000. 
                                // ~ 0 -> 1 , 001 -> 110 -> STREAM OF BITS = # BITS IN THE INPUT
  // wait 1 sec
  _delay_ms(1000);
  // turn the led off
  PORTD = 0x01; 
  // wait 1 sec
  _delay_ms(1000);
}
