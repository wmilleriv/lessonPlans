global _start

section .data
    message db "Hello World", 10
    msg_length equ $-message

section .text
_start:
mov rax, 0x1
mov rdi, 1
mov rsi, message
mov rdx, msg_length
syscall

Exit:
