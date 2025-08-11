global _start

section .data
    welcome db 0dh,0ah, 0dh, 0ah, " Hello ", 0dh, 0ah
    welcome_length equ $-welcome

section .text

_start:

LOOP:

welcome_message:
    mov rax, 0x1 ;set to write
    mov rdi, 1 ;set to stdout
    mov rsi, welcome ;add string to register
    mov rdx, welcome_length ;set string length
    syscall
    ret `;return
