// @author Abdelaziz Salah
// this is the first example 

// importing libraries 
#include <avr/io.h>
#include <util/delay.h> 
void setup() {
// Q/ configure the MC with internal 16MHZ Clock 
// A/ This is the internal default frequency of the clock.
// Configure pin 0 in PORTD as output pin
DDRD = 0x01;

// The Led is connected to pin 0 in PORTD
PORTD = 0x01; // 1 because we work negative logic. 

// Connect the lead using negative logc to flash every 1 second
// Hardware task, connect the resistor to VCC and to the long leg of the led,
// and the short leg connect it to pin 0 on the arduino
}

void loop() {
  // turn the led on 
  PORTD = 0x00; 
  // wait 1 sec
  _delay_ms(1000);
  // turn the led off
  PORTD = 0x01; 
  // wait 1 sec
  _delay_ms(1000);
}
