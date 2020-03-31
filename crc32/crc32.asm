section .text
    global crc32

crc32:
    push rbp
    mov rbp, rsp
    ; initial 0xFFFFFFFF
    xor rax, rax
    mov eax, 0xFFFFFFFF
    ; r10 = rdi = data
    mov r10, rdi
    ; r8 = rsi = length
    mov r8, rsi
    fordata:
        mov r11d, [r10]
        xor al, r11b
        mov cl, 8
        for8:
            mov rdx, rax
            and edx, 1
            sub edx, 1
            xor edx, 0xFFFFFFFF
            ; polynomial
            and edx, 0xEDB88320
            shr eax, 1
            xor rax, rdx
            dec cl
            jnz for8
        inc r10
        dec r8
        jnz fordata
    ; xor at end
    xor eax, 0xFFFFFFFF
    pop rbp
    ret