// @author Abdelaziz Salah 
// @author Saraah El-Zayat

#include <avr/io.h>
#include <avr/interrupt.h>

ISR(INT0_vect) {
// toggling the value of 3rd bit in portD
 PORTC = PORTC ^ (1 << PC0); 
}

void INT0_init(void) {
  // disable all the interrupts 
  SREG &= ~(1 << 7); 

  DDRD = DDRD & (~(1 << PD2)); // defining the direction as input
  EIMSK |= (1 << INT0); //  enabling the external interrupt
  EICRA |= (1 << ISC00) | (1 << ISC01);  // setting 

  // enabling the interrupts
  SREG |= (1 << 7);
}

void setup() {
  // put your setup code here, to run once:
  INT0_init(); 
  DDRC |= (1 << PC0); // setting the direction as output. 
  PORTC |= (1 << PC0); // setting the initial value.
  Serial.begin (9600);  
}

void loop() {
  // put your main code here, to run repeatedly:
  

}
