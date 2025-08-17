.global _start

.section .data
    welcome: .ascii " Hello \n"
    choice: .ascii  "Please enter your selection\n"
    operator: .ascii "1)Add\n 2)Subtract\n 3)Multiply\n 4)Divide\n 5)Exit\n"
    tmp: db 0,0
    first_number: .ascii "Enter first number\n"
    second_number: .ascii "Enter second number\n"
    first_temp: db 0,0
    second_temp: db 0,0
    answer: .ascii "Answer: \n"
    plus: .ascii " + \n"
    equals: .ascii " = \n"
.section .text

_start:
        

LOOP:
    call welcome_message
    call get_choice
    call operators
    call get_input
    call compare_input
    jmp LOOP


compare_input:    
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
    ret ;return

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
    mov rdx, operator_length
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
    mov rsi, second_number
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

    mov r8, [first_temp]
    mov r9, [second_temp]

    sub r8, 48
    sub r9, 48

    mov r10, r8
    add r10, r9

    pop r9
    pop r8

    add r10, 48
    
    mov rax, 0x1
    mov rdi, 1
    mov rsi, answer
    mov rdx, answer_length
    syscall

    mov rax, 0x1
    mov rdi, 1
    mov rsi, r8
    mov rdx, 1
    syscall

    mov rax, 0x1
    mov rdi, 1
    mov rsi, plus
    mov rdx, plus_length
    syscall

    mov rax, 0x1
    mov rdi, 1
    mov rsi, r9
    mov rdx, 1
    syscall

    mov rax, 0x1
    mov rdi, 1
    mov rsi, equals
    mov rdx, equals_length
    syscall
    
    mov [rsp+8], r10    

    mov rax, 0x1
    mov rdi, 1
    lea rsi, [rsp+8]
    mov rdx, 1
    syscall

    jmp LOOP

Subtract:

Multiply:

Divide:

Exit:


