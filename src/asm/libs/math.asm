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

dividir:
    # Extraigo IP
    pop dx
    # Dividendo
    pop ax
    # Divisor
    pop cx
    mov bx, 0
    div_cycle:
        cmp ax, cx
        jle fin_div
        sub ax, cx
        inc bx
        jmp div_cycle
    fin_div:
        push dx
        ret