// @author Abdelaziz Salah 
// @author Khaled Hesham 
// same as example 1 but just use ctc 
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>
// defining global conter 
volatile uint8_t total_overFlow = 0; 

void timer2_init() {
  // setting up the timer with prescaling 1024
  TCCR2B = 0x07; /// because timer 2 in the data sheet work with 00000111. 
  // to activate CTC
  TCCR1A = TCCR1A & (~(1 << 0)); 
  TCCR1A = TCCR1A & (~(1 << 1));
  TCCR1B = TCCR1B | (1<<3); 
  // initializing the counter to 0
  TCNT2 = 0; 

  // activating the intterupt. 
  TIMSK2 = 0x01; 
  sei();
}


ISR  (TIMER2_OVF_vect) { 
  total_overFlow ++; 
}


void setup() {
  // put your setup code here, to run once:
  DDRC = 0x01; // making the portC bit 0 as output
  PORTC |= (1<<PC0); // setting its initial value as 1, positive logic, means 1 is givin a flash. 
  timer2_init(); 

  /// el fekra eny ha5ly kol lama el counter ye3d cycle kamla, ha compare 3leha, w ha3ml call lel ISR, 34an azwd el totalOverFlows.
  OCR2A = 255; // register which carries the counter that we compare on its value. 
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
//  if(!(TIFR1 & (1<<1))){
//    total_overFlow ++; 
//    TCNT2 = 0; 
//  }
  if(total_overFlow > 30) {
    Serial.print("\nEntered32\n"); 
    if(TCNT2 > 8){ // because it is active low. 
      Serial.print("Entered\n"); 
      PORTC ^= (1<<0); 
      total_overFlow = 0; 
      TCNT2 = 0; 
      TIFR1 |= (1<<0); 
    }
  }
}
