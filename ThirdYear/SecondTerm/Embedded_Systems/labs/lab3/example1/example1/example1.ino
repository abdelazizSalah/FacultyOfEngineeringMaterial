// @author Abdelaziz Salah 
// @author Khaled Hesham 
#include <util/delay.h>
#include <avr/io.h>

// defining global conter 
volatile uint8_t total_overFlow = 0; 

void timer0_init() {
  // setting up the timer with prescaling 1024
  TCCR2B = 0x07; /// because timer 2 in the data sheet work with 00000111.  

  // initializing the counter to 0
  TCNT2 = 0; 

  // activating the intterupt. 
  TIMSK2 = 0x01; 
}

ISR  ( TIMER2_OVF_vect) {
  total_overFlow ++; 
}

void setup() {
  // put your setup code here, to run once:
  DDRC = 0x01; // making the portC bit 0 as output
  PORTC |= (1<<PC0); // setting its initial value as 1, positive logic, means 1 is givin a flash. 
  timer0_init(); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(total_overFlow > 30) {
    if(TCNT2 > 8){
      PORTC ^= 0x01; 
      total_overFlow = 0; 
      TCNT2 = 0; 
    }
  }
}
