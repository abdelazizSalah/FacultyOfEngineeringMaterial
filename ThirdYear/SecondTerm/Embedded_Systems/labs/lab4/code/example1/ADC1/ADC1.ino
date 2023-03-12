// @author Abdelaziz Salah
// @author Khaled Hesham
// Example 1
#include <avr/io.h> 

uint16_t adc_read (uint8_t channel) {
  channel &= 0x07;
  ADMUX = (ADMUX & 0xF8) | channel;

  // start conversion 
  ADCSRA |= (1<<ADSC); 

  // wait till the conversion is done 
  while (ADCSRA & (1<<ADSC)); 

  return (ADC); 
}

void setup () {
  // setting AREF = AVcc
  ADMUX = (1<<REFS0); 

  // enabling the adc 
  ADCSRA = (1<< ADEN); 

  // setting the prescaler to 128
  ADCSRA |= 0x07; 

  // setting the serial baud rate
  Serial.begin(9600); 

  // initializing the ADC
}


void loop () {
  Serial.print(adc_read(0)); 
  Serial.print('\n');
}
