global _start

section .data
    welcome db 0dh,0ah, 0dh, 0ah, " Hello ", 0dh, 0ah
    welcome_length equ $-welcome
    choice db "Please enter your selection", 0dh, 0ah
    choice_length equ $-choice
    operator db "1) Addition",0dh,0ah, "2) Subtraction", 0dh, 0ah, "3) Multiplication", odh, 0ah, "4) Division" odh, 0ah, "5) Exit",10
    operator_length equ $-operator
section .text

_start:

LOOP:
    call welcome_message
    call get_choice
    call operators

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
