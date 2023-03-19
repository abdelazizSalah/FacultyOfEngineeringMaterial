#include <avr/io.h>
#include <avr/interrupt.h>
#include <Arduino.h>

// init spi as Master
void spi_init_master(void)
{
    // Set MOSI and SCK output, all others input
    DDRB = (1 << DD3) | (1 << DD2) | (1 << DD5);

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
    return SPDR;
}

int main(void)
{
    spi_init_master();
    Serial.begin(9600);
    _delay_ms(1000);

    int i = 1;
    while (1)
    {
        i = spi_write_read(i);
        Serial.println(i);
        _delay_ms(1000);
    }
}
