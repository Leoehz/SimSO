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
    pop bx
    pop cx
    mov ax, 0
    mov dx, 0
    cycle:
        add ax, cx
        inc dx
        cmp ax, bx
        jnz cycle2
        jle cycle
        jmp cycle3
    cycle2:
        push dx
        push 0
    cycle3:
        dec dx
        push dx
        mov dx, 0
        dec ax
        inc dx
        cmp ax, bx
        jnz end
        jmp cycle3
    end:
        push dx
    ret

raiz_cuadrada:
    noop