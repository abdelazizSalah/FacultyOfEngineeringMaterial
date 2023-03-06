// @author Abdelaziz Salah
// @author Khaled Hesham 
#include<avr/io.h>
#include<avr/interrupt.h>

volatile uint8_t tot_overflow;
volatile unsigned char segment_values[10] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};
int cnt = 0;
  // TIMER0 overflow interrupt service routine// called whenever TCNT0 overflows
ISR(TIMER2_OVF_vect)
{
  // keep a track of number of overflows
  tot_overflow++;
}

void timer2_init(){
  // set up timer with prescaler = 1024
  TCCR2B |= (1 << CS20) | (1 << CS21) | (1 << CS22);
  // initialize counter
  TCNT2 = 0;
  // enable overflow interrupt
  TIMSK2 |= (1 << TOIE2);
  // enable global interrupts
  sei();
  // initialize overflow counter variable
  tot_overflow = 0; 
}


void setup() {
  // put your setup code here, to run once:
  DDRD |= 0xff; // define all of port D as 1
  DDRC |= (1 << PC0) || (1 << PC1);
  timer2_init();
  PORTD = 0; 
  PORTC = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  if (tot_overflow >= 60) // NOTE: '>=' is used{
    // check if the timer count reaches 53
    if (TCNT2 >= 8){ 
      PORTD = segment_values[(cnt)%10];
      PORTC = segment_values[(cnt++)%10];

      TCNT2 = 0;
      tot_overflow = 0; // toggles the ledTCNT0 = 0; // reset countertot_overflow = 0; // reset overflow counter}
    }
}
