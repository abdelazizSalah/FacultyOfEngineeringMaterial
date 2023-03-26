/// @Author Abdelaziz Salah
/// @Author Mahmoud Reda.
/// @Date 26/3/2023

// pin mask definition
//const _GPIO_PINMASK_ALL = 0XFFFF;    -> predefined.
//void main() {
 // defining the output pins
 /// we define it on port D and E
// GPIO_DIGITAL_OUTPUT(&GPIOD_BASE, _GPIO_PINMASK_ALL);
// GPIO_DIGITAL_OUTPUT(&GPIOE_BASE, _GPIO_PINMASK_ALL);
// GPIOD_ODR = 0;
// GPIOE_ODR = 0;
 // void loop
 //while (1) {
  //  GPIOD_ODR = ~GPIOD_ODR;
   // GPIOE_ODR = ~GPIOE_ODR;
    //Delay_ms(500);
 //}
 //return ;
//}

/// @author Abdelaziz Salah
/// @author Mahmoud Reda
/// @date 26/3/2023

// example 2
//int i = 0;
//void shift(int seed)
//{
//     counter = seed/
//    / for (i = 0 ; i < 4; i++){
//    / delay (500) ms
//    / portD |= counter;
//    / counter <<= 1;
//     }
//    int counter = seed;
//    for (i = 0; i < 4; i++) {
//       Delay_ms(500);
//       GPIOD_ODR |= counter ;    // oring
//       GPIOE_ODR |= counter ;
//       counter <<= 1;
//    }
//}
//
//void deshift(int seed) {
// int counter = seed;
//     for (i = 0; i < 4; i++){
//       Delay_ms(500);
//       GPIOD_ODR &= counter;   // anding
//       GPIOE_ODR &= counter ;
//       counter <<= 1;
//     }
//}
//
// void seed (int seed) {
     // put the seed into the ports we want to work on
     // portD = seed
     // portE = seed
// }
//
// void setup
// int seed1 = 0x1111;
// int seed2 = 0xEEEE;
//
//void main()
//{
// GPIO_DIGITAL_OUTPUT(&GPIOD_BASE, _GPIO_PINMASK_ALL);
// GPIO_DIGITAL_OUTPUT(&GPIOE_BASE, _GPIO_PINMASK_ALL);
// GPIOD_ODR = 0;
// GPIOE_ODR = 0;
//
    // void loop
//    while (1)
//    {
//        shift(seed1);
//
//        deshift(seed2);
//    }
//}

// Example 3
int counter = 0;
void main (){
 // configure PB0 and PB1 as input
 GPIO_Digital_Input (&GPIOB_BASE, _GPIO_PINMASK_0 |_GPIO_PINMASK_1 );
 // THIS IS THE INCREMENTER PB0
// Button (&GPIOB_IDR,0,50,1) ;
 
 // THIS IS THE DECREMENTER
// Button (&GPIOB_IDR,1, 50, 1);

 // define portD low as output
 GPIO_DIGITAL_OUTPUT(&GPIOD_BASE, _GPIO_PINMASK_LOW);
 // INITIALLY TURNED OFF.
 GPIOD_ODR = 0x00ff;

 // VOID LOOP
 while (1) {
   if(Button (&GPIOB_IDR,0,30,1)){
    // pb0 is pressed
    // increment
    if(counter == 15)
        counter = 15;
    else
        counter ++ ;
    while(Button (&GPIOB_IDR,0,30,1));
   }

   if(Button (&GPIOB_IDR,1, 30, 1)){
    // pb1 is pressed
    // decrement
    if(counter == 0)
        counter = 0;
    else
        counter --;
    /// this is how we can make it work only on the raising edge :)
    /// because while the result is one so we won't do any thing till we have reset the bit
    /// and when it raise again to one, this will be a new raising edge.
    /// can you make it work on the falling edge ? :)
    while(Button (&GPIOB_IDR,1,30,1));
   }
   GPIOD_ODR = counter ;
 }
}

//void main() {
//      int counter=0;
//
//
//      GPIO_Digital_Input(&GPIOB_BASE, _GPIO_PINMASK_0 | _GPIO_PINMASK_1);
//      GPIO_Digital_Output(&GPIOD_BASE, _GPIO_PINMASK_0 | _GPIO_PINMASK_1 | _GPIO_PINMASK_2 | _GPIO_PINMASK_3);
//      while(1){
//
//      GPIOD_ODR=counter;
//
//      if(  Button(&GPIOB_IDR, 0, 2, 1)){
//               PB0 clicked
//              if(counter != 15 ){
//                      counter=counter+1;
//                      Delay_ms(500);
//
//              }
//
//      }
//      while( Button(&GPIOB_IDR, 0, 2, 1)){}
//
//
//      if( Button(&GPIOB_IDR, 1, 2, 1)){
//                PB1 clicked
//               if(counter!=0){
//                counter=counter -1;
//                Delay_ms(500);
//               }
//
//      }
//            while(Button(&GPIOB_IDR, 1, 2, 1)){}
//
//      }
//
// }