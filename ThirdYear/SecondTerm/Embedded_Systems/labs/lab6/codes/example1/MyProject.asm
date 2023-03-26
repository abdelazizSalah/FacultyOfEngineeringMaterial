_main:
;MyProject.c,1 :: 		void main () {
;MyProject.c,2 :: 		GPIOA_ODR = 0XFFFF;
MOVW	R1, #65535
MOVW	R0, #lo_addr(GPIOA_ODR+0)
MOVT	R0, #hi_addr(GPIOA_ODR+0)
STR	R1, [R0, #0]
;MyProject.c,3 :: 		}
L_end_main:
L__main_end_loop:
B	L__main_end_loop
; end of _main
