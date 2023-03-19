#include <avr/io.h>
#include <avr/interrupt.h>
#include <Arduino.h>

// init spi as Slave
void spi_init_slave(void)
{
    // Set MISO output, all others input
    DDRB |= (1 << DD4);
    DDRB &= ~((1 << DD3) | (1 << DD2) | (1 << DD5));

    // Enable SPI
    SPCR = (1 << SPE);
}

// spi write and read
uint8_t spi_write_read(uint8_t data)
{
    // Start transmission
     SPDR= data;
    // Wait for transmission complete
    while (!(SPSR & (1 << SPIF)))
        ;
    return SPDR;
}

int main(void)
{
    spi_init_slave();
    Serial.begin(9600);
    int i = 0;
    while (1)
    {
        i = spi_write_read(i);
        Serial.println(i);
        i += 100;
        _delay_ms(1000);
    }
}
