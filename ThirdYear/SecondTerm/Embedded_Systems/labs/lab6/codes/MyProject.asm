_main:
;MyProject.c,84 :: 		void main (){
;MyProject.c,86 :: 		GPIO_Digital_Input (&GPIOB_BASE, _GPIO_PINMASK_0 |_GPIO_PINMASK_1 );
MOVW	R1, #3
MOVW	R0, #lo_addr(GPIOB_BASE+0)
MOVT	R0, #hi_addr(GPIOB_BASE+0)
BL	_GPIO_Digital_Input+0
;MyProject.c,94 :: 		GPIO_DIGITAL_OUTPUT(&GPIOD_BASE, _GPIO_PINMASK_LOW);
MOVW	R1, #255
MOVW	R0, #lo_addr(GPIOD_BASE+0)
MOVT	R0, #hi_addr(GPIOD_BASE+0)
BL	_GPIO_Digital_Output+0
;MyProject.c,96 :: 		GPIOD_ODR = 0x00ff;
MOVS	R1, #255
MOVW	R0, #lo_addr(GPIOD_ODR+0)
MOVT	R0, #hi_addr(GPIOD_ODR+0)
STR	R1, [R0, #0]
;MyProject.c,99 :: 		while (1) {
L_main0:
;MyProject.c,100 :: 		if(Button (&GPIOB_IDR,0,30,1)){
MOVS	R3, #1
MOVS	R2, #30
MOVS	R1, #0
MOVW	R0, #lo_addr(GPIOB_IDR+0)
MOVT	R0, #hi_addr(GPIOB_IDR+0)
BL	_Button+0
CMP	R0, #0
IT	EQ
BEQ	L_main2
;MyProject.c,103 :: 		if(counter == 15)
MOVW	R0, #lo_addr(_counter+0)
MOVT	R0, #hi_addr(_counter+0)
LDRSH	R0, [R0, #0]
CMP	R0, #15
IT	NE
BNE	L_main3
;MyProject.c,104 :: 		counter = 15;
MOVS	R1, #15
SXTH	R1, R1
MOVW	R0, #lo_addr(_counter+0)
MOVT	R0, #hi_addr(_counter+0)
STRH	R1, [R0, #0]
IT	AL
BAL	L_main4
L_main3:
;MyProject.c,106 :: 		counter ++ ;
MOVW	R1, #lo_addr(_counter+0)
MOVT	R1, #hi_addr(_counter+0)
LDRSH	R0, [R1, #0]
ADDS	R0, R0, #1
STRH	R0, [R1, #0]
L_main4:
;MyProject.c,107 :: 		while(Button (&GPIOB_IDR,0,30,1));
L_main5:
MOVS	R3, #1
MOVS	R2, #30
MOVS	R1, #0
MOVW	R0, #lo_addr(GPIOB_IDR+0)
MOVT	R0, #hi_addr(GPIOB_IDR+0)
BL	_Button+0
CMP	R0, #0
IT	EQ
BEQ	L_main6
IT	AL
BAL	L_main5
L_main6:
;MyProject.c,108 :: 		}
L_main2:
;MyProject.c,110 :: 		if(Button (&GPIOB_IDR,1, 30, 1)){
MOVS	R3, #1
MOVS	R2, #30
MOVS	R1, #1
MOVW	R0, #lo_addr(GPIOB_IDR+0)
MOVT	R0, #hi_addr(GPIOB_IDR+0)
BL	_Button+0
CMP	R0, #0
IT	EQ
BEQ	L_main7
;MyProject.c,113 :: 		if(counter == 0)
MOVW	R0, #lo_addr(_counter+0)
MOVT	R0, #hi_addr(_counter+0)
LDRSH	R0, [R0, #0]
CMP	R0, #0
IT	NE
BNE	L_main8
;MyProject.c,114 :: 		counter = 0;
MOVS	R1, #0
SXTH	R1, R1
MOVW	R0, #lo_addr(_counter+0)
MOVT	R0, #hi_addr(_counter+0)
STRH	R1, [R0, #0]
IT	AL
BAL	L_main9
L_main8:
;MyProject.c,116 :: 		counter --;
MOVW	R1, #lo_addr(_counter+0)
MOVT	R1, #hi_addr(_counter+0)
LDRSH	R0, [R1, #0]
SUBS	R0, R0, #1
STRH	R0, [R1, #0]
L_main9:
;MyProject.c,117 :: 		while(Button (&GPIOB_IDR,1,30,1));
L_main10:
MOVS	R3, #1
MOVS	R2, #30
MOVS	R1, #1
MOVW	R0, #lo_addr(GPIOB_IDR+0)
MOVT	R0, #hi_addr(GPIOB_IDR+0)
BL	_Button+0
CMP	R0, #0
IT	EQ
BEQ	L_main11
IT	AL
BAL	L_main10
L_main11:
;MyProject.c,118 :: 		}
L_main7:
;MyProject.c,119 :: 		GPIOD_ODR = counter ;
MOVW	R0, #lo_addr(_counter+0)
MOVT	R0, #hi_addr(_counter+0)
LDRSH	R1, [R0, #0]
MOVW	R0, #lo_addr(GPIOD_ODR+0)
MOVT	R0, #hi_addr(GPIOD_ODR+0)
STR	R1, [R0, #0]
;MyProject.c,120 :: 		}
IT	AL
BAL	L_main0
;MyProject.c,121 :: 		}
L_end_main:
L__main_end_loop:
B	L__main_end_loop
; end of _main
