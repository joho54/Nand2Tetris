    @n
    M=0
    @R2
    M=0

(LOOP)
    // n 증가
    @n
    M=M+1

    //n 비교, 루프
    D=M
    @R1
    D=M-D
    @END
    D;JLT

    // ans = ans + r0
    @R0
    D=M
    @R2
    M=D+M

    @LOOP
    0;JMP

(END)
    @END
    0;JMP

