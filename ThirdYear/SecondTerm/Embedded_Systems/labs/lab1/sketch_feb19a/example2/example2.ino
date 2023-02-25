// @author Abdelaziz Salah 
// Example two

// including libraries 
#include <avr/io.h>
#include <util/delay.h>

void setup() {
 // Switch one and two are connected on pin 0 and 1 in PortB, so they should be inputs
 DDRB = DDRB & ( ~(1 << PB1)); 
 DDRB = DDRB & ( ~(1 << PB0));  // or we could simply defined it as 0xFC as C is 1100 so we will set it to input


 // Led 1 and 2 are defined on pin 0 and 1 in PORTC, so we should define them as output

 DDRC = DDRC | ((1 << PC1)); 
 DDRC = DDRC | ((1 << PC0));  // or we could simply defined it as 0xFC as C is 1100 so we will set it to input

 
 PORTC = PORTC &(~(1 << PC1)); 
 PORTC = PORTC & (~(1 << PC0)); // this by default input, but for my knowleadge and practice I wrote it. 
 Serial.begin(9600);
}

void loop() {
  // if switch 1 is pressed turn on the led
  if (PINB & (1<<PB1)){ // 00000010 
    PORTC = PORTC | (1<<PC0); 
    Serial.print("in");
  } else {
    PORTC = PORTC & (~(1<<PC0)); 
  }
   // not else because we want if both are pressed they should light. 
   if (PINB & (1 << PB0)){ // 00000001
    PORTC = PORTC | (1<<PC1); 
  } else {
    PORTC = PORTC & (~(1<<PC1)); 
  }
}
