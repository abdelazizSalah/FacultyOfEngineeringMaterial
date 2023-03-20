#include <avr/io.h>
#include <avr/interrupt.h>
#include <Arduino.h>

// init spi as Master
void spi_init_master(void)
{
  // Set MOSI and SCK output, all others input
  DDRB |= (1 << DD3) | (1 << DD2) | (1 << DD5);

  DDRB &= ~(1 << DD4);

  // make sure SS is high
  PORTB |= (1 << DD2);

  // Enable SPI, Master, set clock rate fck/16
  SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR0);
}

// spi write and read
uint8_t spi_write_read(uint8_t data)
{
  // Start transmission
  SPDR = data;
  // Wait for transmission complete
  while (!(SPSR & (1 << SPIF)))
    ;
  uint8_t kk = SPDR;
  return kk;
}

void spi_write(uint8_t data)
{
  // Start transmission
  SPDR = data;
  // Wait for transmission complete
  while (!(SPSR & (1 << SPIF)))
    ;
  volatile char kk = SPDR;
  kk += 1;
  // return kk;
}

uint8_t spi_read(void)
{
  // Start transmission
  SPDR = 0xFF;
  // Wait for transmission complete
  while (!(SPSR & (1 << SPIF)))
    ;
  uint8_t kk = SPDR;
  return kk;
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
