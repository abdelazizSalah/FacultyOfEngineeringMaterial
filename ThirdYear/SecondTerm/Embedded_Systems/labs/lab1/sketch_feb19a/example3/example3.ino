// @Author Abdelaziz Salah 
// Example 3

// including libraries 
#include <avr/io.h> 
#include <util/delay.h>
void setup() {
  // set pin 0 in PORTB as input pin aand use the internal pull up resistor
  DDRB = DDRB & (~(1 <<PB0)); 
  PORTB = PORTB | (1 << PB0); 

  // configure pin 0 of port C as output pin 
  DDRC = 0x01;
  // make led off at beginning
  PORTC = PORTC | (1 << PC0) ; 
  Serial.begin(9600); 
}

void loop() {
  if ((PINB & 0b00000001)  != 1) {
    _delay_ms(100); 
    Serial.print("in");
    if((PINB & 0b00000001)!=1) { // if not working make it 1
      PORTC = PORTC ^ (1 << PC0);
    Serial.print("dkhlt");
    }
  }
}
