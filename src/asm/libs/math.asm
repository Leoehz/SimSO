multiplicar:
    pop bx
    pop cx
    pop dx
    mov ax, 0
    mult_cycle:
        add ax, cx
        dec dx
        cmp dx, 0
        jnz mult_cycle
    push bx
    ret
