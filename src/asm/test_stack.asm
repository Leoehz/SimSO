sumar:
    pop bx
    pop cx
    pop dx
    push bx
    add cx, dx
    mov ax, cx
    ret
main:
    inc ax
    inc ax
    inc bx
    cmp ax, bx
    cmp ax, 2
    dec ax
    call sumar
    jmp main