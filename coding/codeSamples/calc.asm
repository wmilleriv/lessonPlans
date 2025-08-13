global _start

section .data
    welcome db 0dh,0ah, 0dh, 0ah, " Hello ", 0dh, 0ah
    welcome_length equ $-welcome
    choice db "Please enter your selection", 0dh, 0ah
    choice_length equ $-choice
    operator db "1) Addition",0dh,0ah, "2) Subtraction", 0dh, 0ah, "3) Multiplication", odh, 0ah, "4) Division" odh, 0ah, "5) Exit",10
    operator_length equ $-operator
    tmp db 0,0
    first_number db "Enter first number", 0dh, 0ah
    first_number_length equ $-first_number
    second_number db "Enter second number", 0dh, 0ah
    second_number_length equ $-second_number

section .text

_start:
        

LOOP:
    call welcome_message
    call get_choice
    call operators
    
    cmp byte[rsi], '1'
    je Add
    
    cmp byte[rsi], '2'
    je Subtract
    
    cmp byte[rsi], '3'
    je Multiply
    
    cmp byte[rsi], '4'
    je Divide
    
    cmp byte[rsi], '5'
    je Exit
    
welcome_message:
    mov rax, 0x1 ;set to write
    mov rdi, 1 ;set to stdout
    mov rsi, welcome ;add string to register
    mov rdx, welcome_length ;set string length
    syscall
    ret `;return

get_choice:
    mov rax, 0x1
    mov rdi, 1
    mov rsi, choice
    mov rdx, choice_length
    syscall
    ret

operators:
    mov rax, 0x1
    mov rdi, 1
    mov rsi, operator
    mov rdx operator_length
    syscall
    ret

get_input:
    mov rax, 0 ;set to read
    mov rdi, 0 ;set to stdin
    mov rsi, tmp 
    mov rdx, 2 ;2 bytes allocated, 1 for number, 1 for newline
    syscall

Add:
    mov rax, 0x1
    mov rdi, 1
    mov rsi, first_number
    mov rdx, first_number_length
    syscall

    mov rax, 0
    mov rdi, 0 
    mov rsi, first_temp ;   
    mov rdx, 2
    syscall

    mov r8, first_temp
    
    mov rax, 0x1
    mov rdi, 1
    mov rsi, second__number
    mov rdx, second_number_length
    syscall

    mov rax, 0
    mov rdi, 0 
    mov rsi, second_temp ;   
    mov rdx, 2
    syscall

    mov r9, second_temp

    push r8
    push r9 ;move registers holding values to stack
