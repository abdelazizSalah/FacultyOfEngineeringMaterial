// @Author Abdelaziz Salah
// @Author Ahmed Atta 
// @date 19/3/2023
// this file contains the master implementation for SPI protocol.
#include <avr/io.h>
#include <avr/interrupt.h>
#include <Arduino.h>

// init spi as Master
void spi_init_master(void)
{
  // Make MOSI, SCK and SS as output for the master. 
  DDRB |= (1 << DD3) | (1 << DD2) | (1 << DD5); // of you can define them as we will see in the slave code. 

  // setting the defining MISO pin as input.
  DDRB &= ~(1 << DD4);

  // make sure SS is high to avoid selecting any slaves for now.  
  PORTB |= (1 << DD2);

  // Enable SPI, Master, set clock rate fck/16 -> no doubling for the frequency. 
  SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR0);
}

void spi_write(uint8_t data)
{
  // Start transmission
  SPDR = data; 
  // Wait for transmission complete
  while (!(SPSR & (1 << SPIF)));
  volatile char flush_buffer = SPDR;
  flush_buffer += 1; // no need but to make sure that it is working correctly during the lab. 
}

uint8_t spi_read(void)
{
  // Start transmission
  SPDR = 0xFF; // just dummy data, to start the transmission as we mentioned in the lab explaination.
  // Wait for transmission complete
  while (!(SPSR & (1 << SPIF)));
  uint8_t flush_buffer = SPDR;  // we can directly return SPDR, but Atta prefered this way :D. 
  return flush_buffer;
}

int main(void)
{
  Serial.begin(9600);

  spi_init_master();
  PORTB &= ~(1 << DD2); // select slave
  // volatile char kk = SPDR;
  // kk += 1;
  _delay_ms(300);
  uint8_t i = 1;
  while (1)
  {
    if (i > 100)
      i = 1;
    // uint8_t t = spi_write_read(i++);
    spi_write(i++);
    _delay_ms(10);
    // i += 100;
    uint8_t t = spi_read();
    Serial.println(t);
    _delay_ms(300);
  }
}
