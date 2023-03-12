// @author Abdelaziz Salah
// @author Khaled Hesham
// Example2-3 - use the leds to give the binary representation 000,001,010,011 ... 111- using ISR
#include <avr/io.h> 
#include <avr/interrupt.h>

// flag that indicate the end of conversion
uint8_t endConversionFlag = 0; 

uint16_t adc_read (uint8_t channel) {
  // setting the channel
  channel &= 0x07;
  ADMUX = (ADMUX & 0xF8) | channel;

  // start conversion 
  ADCSRA |= (1<<ADSC); 

  // wait till the conversion is done 
  while (ADCSRA & (1<<ADSC)); 

  // return after ISR execution
  if(endConversionFlag) {
    endConversionFlag = 0; 
    return (ADC); 
  } else 
    return -1; 
}


// defining the interupt service routine for the ADC
ISR (ADC_vect){
   endConversionFlag = 1; 
}

void setup () {
  // setting AREF = AVcc
  ADMUX = (1<<REFS0); 

  // enabling the adc 
  ADCSRA = (1<< ADEN); 

  // setting the prescaler to 128
  ADCSRA |= 0x07; 

  // setting the interupt enable of the adc 
  ADCSRA |= (1<<ADIE); 
  
  // setting the serial baud rate
  Serial.begin(9600); 

  // setting the global interrupt
  sei(); 

  // setting 3 pins as output 
  DDRB = 0x07; 
}


void loop () {

  uint16_t adcResult = adc_read(0); 
  if(adcResult != -1){
    // this equation is used to normalize the value to be in a result between 0-1
    // then multiply by 8 to get 1 of 8 values [0-7]
    // then assigning the int of the result to get their binary representation.
    PORTB = (int) (adcResult / 1024.0 * 8); 
  }
}
