#include <avr/io.h>
#include <avr/interrupt.h>
#include <Arduino.h>
#define SS PB2
#define SCLK PB5
#define MOSI  PB3
#define MISO PB4
// init spi as Slave
void spi_init_slave(void)
{
    // Set MISO output, all others input
    DDRB |= (1 << MISO);
    DDRB &= ~((1 << MOSI) | (1 << SCK) | (1 << SS)); // defining them as input. 

    // Enable SPI
    SPCR = (1 << SPE);
}

// spi write and read
void spi_write(uint8_t data)
{
    volatile char flush_buffer; 
    // Start transmission
    SPDR= data;
    // Wait for transmission complete
    while (!(SPSR & (1 << SPIF)));
    flush_buffer = SPDR;
    
}

char spi_read () {
    SPDR = 0xFF; 
    // Wait for transmission complete
    while (!(SPSR & (1 << SPIF)));
    return SPDR; 
}

int main(void)
{
    spi_init_slave();
    Serial.begin(9600);
    uint8_t dataSend = 0;
    uint8_t dataRec = 0; 
    while (1)
    {
        // read first 
        dataRec = spi_read();
        Serial.println(dataRec);
        // then write 
        dataRec +=100; 
        spi_write(dataRec);  
    }
}
