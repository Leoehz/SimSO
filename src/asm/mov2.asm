main:
    mov ax, 1
    mov ax, 2
    mov ax, 5
    mov bx, 10
test:
    mov cx, ax
    mov ax, bx
    mov ax, 8
    jmp test