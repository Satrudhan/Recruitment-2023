DATA SEGMENT USE16
    NUM1 DW  120          ; NUmber of stones per KM
    NUM2 DW  48             ; Length of bridge in KM
    RESULT DW ?        ; Variable to store the result
    MSG DB 'TOtal number of stones: $'
DATA ENDS

CODE SEGMENT USE16
    ASSUME CS:CODE, DS:DATA

BEG:
    MOV AX, DATA       ; Load the data segment address into AX
    MOV DS, AX         ; Set DS to point to the data segment

    MOV AX, [NUM1]     ; Load the first number into AX
    MUL WORD PTR [NUM2] ; Multiply AX by the second number
    MOV [RESULT], AX   ; Store the result in RESULT

    MOV AH, 9          ; Print the message
    MOV DX, OFFSET MSG ; Load the offset of the message into DX
    INT 21H

    MOV AX, [RESULT]   ; Load the result into AX
    MOV BX, 10         ; Divisor for division by 10
    XOR CX, CX         ; Clear CX for digit counting

convert_loop:
    XOR DX, DX         ; Clear DX for division
    DIV BX             ; Divide AX by 10, quotient in AX, remainder in DX
    PUSH DX            ; Push the remainder onto the stack
    INC CX             ; Increment digit count

    OR AX, AX          ; Check if quotient is zero
    JNZ convert_loop   ; If not zero, continue conversion

    print_loop:
    POP DX             ; Pop the remainder from the stack
    ADD DL, '0'        ; Convert the remainder to ASCII
    MOV AH, 2          ; Print the digit
    INT 21H

    LOOP print_loop    ; Repeat for all digits

    MOV AH, 4CH        ; Exit program
    INT 21H

CODE ENDS
END BEG
