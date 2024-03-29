// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.
```
(WHITE)

@512
D=A
@n
M=D
@m
M=0
(LOOP1)
@m
D=M
@SCREEN
A=D+A
M=0
@m
M=M+1

@KBD
D=M
@BLACK
D;JNE

@n
D=M
@m
D=D-M
@LOOP1
D;JGT
@END
0;JMP


(BLACK)

@512
D=A
@n
M=D
@m
M=0
(LOOP2)
@m
D=M
@SCREEN
A=D+A
M=-1
@m
M=M+1

@KBD
D=M
@WHITE
D;JEQ


@n
D=M
@m
D=D-M
@LOOP2
D;JGT
@END
(END)

@END
0;JMP
```

