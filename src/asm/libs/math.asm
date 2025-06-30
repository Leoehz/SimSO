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
    # Seteo en 0 el cociente inicial
    mov bx, 0
    div_cycle:
        cmp ax, cx
        jle fin_div
        sub ax, cx
        inc bx
        jmp div_cycle
    fin_div:
        push dx
        # Se devuelve el resultado, en ax queda el resto y en bx queda el cociente.
        ret

raiz_cuadrada:
    # Extraigo IP
    pop dx
    mov bx, 1
    mov ax, 0
    pop cx
    push bx
    push cx
    mov cx, 1
    multiplica:
        add ax, cx
        dec bx
        cmp bx, 0
        jnz multiplica
        pop cx
        cmp ax, cx
        jle continuar
        jmp fin
    continuar:
        pop bx
        inc bx
        push bx
        push cx
        mov cx, bx
        mov ax, 0
        jmp multiplica
    fin:
        # devuelve el resultado entero más cercano hacia abajo en bx
        pop bx
        dec bx
        push dx
    ret