.global _start

.section .data
message:  "Hello World" 0dh,0ah

.section .text
_start:
    mov $1, %rax
    mov $1, %rdi
    mov $message, %rsi
    mov $15, %rdx
    syscall
        
    mov $60, %rax
    mov $0, %rdi
    syscall

