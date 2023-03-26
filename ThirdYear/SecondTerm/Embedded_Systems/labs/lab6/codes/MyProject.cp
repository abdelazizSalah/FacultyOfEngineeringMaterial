#line 1 "C:/GitHub/FacultyOfEngineeringMaterial/ThirdYear/SecondTerm/Embedded_Systems/labs/lab6/codes/MyProject.c"
#line 83 "C:/GitHub/FacultyOfEngineeringMaterial/ThirdYear/SecondTerm/Embedded_Systems/labs/lab6/codes/MyProject.c"
int counter = 0;
void main (){

 GPIO_Digital_Input (&GPIOB_BASE, _GPIO_PINMASK_0 |_GPIO_PINMASK_1 );







 GPIO_DIGITAL_OUTPUT(&GPIOD_BASE, _GPIO_PINMASK_LOW);

 GPIOD_ODR = 0x00ff;


 while (1) {
 if(Button (&GPIOB_IDR,0,30,1)){


 if(counter == 15)
 counter = 15;
 else
 counter ++ ;
 while(Button (&GPIOB_IDR,0,30,1));
 }

 if(Button (&GPIOB_IDR,1, 30, 1)){


 if(counter == 0)
 counter = 0;
 else
 counter --;
 while(Button (&GPIOB_IDR,1,30,1));
 }
 GPIOD_ODR = counter ;
 }
}
