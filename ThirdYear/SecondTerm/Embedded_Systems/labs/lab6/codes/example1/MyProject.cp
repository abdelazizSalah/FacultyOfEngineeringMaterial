#line 1 "C:/GitHub/FacultyOfEngineeringMaterial/ThirdYear/SecondTerm/Embedded_Systems/labs/lab6/codes/example1/MyProject.c"
void main() {
 int counter=0;


 GPIO_Digital_Input(&GPIOB_BASE, _GPIO_PINMASK_0 | _GPIO_PINMASK_1);
 GPIO_Digital_Output(&GPIOD_BASE, _GPIO_PINMASK_0 | _GPIO_PINMASK_1 | _GPIO_PINMASK_2 | _GPIO_PINMASK_3);
 while(1){

 GPIOD_ODR=counter;

 if( Button(&GPIOB_IDR, 0, 2, 1)){

 if(counter != 15 ){
 counter=counter+1;
 Delay_ms(500);

 }

 }
 while( Button(&GPIOB_IDR, 0, 2, 1)){}


 if( Button(&GPIOB_IDR, 1, 2, 1)){

 if(counter!=0){
 counter=counter -1;
 Delay_ms(500);
 }

 }
 while(Button(&GPIOB_IDR, 1, 2, 1)){}

 }

 }
