// @author Abdelaziz Salah 
// @author Saraah El-Zayat

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
ISR(INT1_vect) {
// toggling the value of 3rd bit in portD
 int count = 5; 
 while(count--) {
  lightingAllTheLeds(); 
 }
}

void INT1_init(void) {
  // disable all the interrupts 
  SREG &= ~(1 << 7); 

  DDRD = DDRD & (~(1 << PD3)); // defining the direction as input
  PORTD |= (1 << PD3);
  EIMSK |= (1 << INT1); //  enabling the external interrupt
  EICRA |= (1 << ISC10) | (1 << ISC11);  // setting 

  // enabling the interrupts
  SREG |= (1 << 7);
}

void setup() {
  // put your setup code here, to run once:
  INT1_init(); 
  DDRC |= (1 << PC0) | (1 << PC1)  | (1 << PC2)  ; // setting the direction as output. 
//  PORTC |= (1 << PC0)| (1 << PC1)  | (1 << PC2); // setting the initial value.
  Serial.begin (9600);  
}

void lightingTheLed(int portNo) {
  PORTC = 0x00; // turning off all the leds
  PORTC |= (1 << portNo); 
  _delay_ms(500);
}
void lightingAllTheLeds() {
  PORTC = 0x07; // turning off all the leds 
  _delay_ms(500);
  PORTC = 0x00;
  _delay_ms(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0 ; i < 3 ; i++) {
    lightingTheLed(i); 
  }
}
