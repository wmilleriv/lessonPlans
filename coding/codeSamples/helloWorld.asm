.section .text
    .global _start
_start:
    mov $4,%rax
    mov $1,%rbx
    mov $message,%ecx
    mov msglength,%edx
    int  $0x80

    mov $1, %rax
    mov $0, %ebx
    int $0x80
.section .data
    message db "Hello world!", 0dh, 0ah
    msglength: equ $-message
