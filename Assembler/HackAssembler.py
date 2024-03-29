import sys
import Parser as p
import Code as c
import SymbolTable as st

class HackAssembler():
    def __init__(self, asm):
        self.asm = asm
        self.process()
        self.p = p.Parser(self.asm)
        self.c = c.Code()
        self.st = st.SymbolTable()
        self.bin = []
        self.digitTable = ['0', '1', '2', '3','4','5','6','7','8','9']
        self.lineNumber = -1
        self.pass1Result = []
        self.pass2Result = []
        self.pass1()
        self.p = p.Parser(self.pass1Result)
        self.pass2()
        self.p = p.Parser(self.pass2Result)
        self.pass3()
        self.serve()
        
    def process(self):
        for i in range(len(self.asm)):
            if self.asm[i][len(self.asm[i])-1:] == '\n':
                self.asm[i] = self.asm[i][:-1]
            self.asm[i] = self.asm[i].strip()
    
    def serve(self):
        for i in range(len(self.bin)):
            self.bin[i] = self.bin[i] + '\n'
    
    def pass1(self):
        while self.p.hasMoreLines():
            self.p.advance()
            if self.p.currentInstruction == None:
                continue
            
            if self.p.instructionType() == 'C_INSTRUCTION' or self.p.instructionType() == 'A_INSTRUCTION':
                self.lineNumber += 1
            
            if self.p.instructionType() == 'L_INSTRUCTION':
                self.st.addEntry(self.p.symbol(), str(self.lineNumber+1))
            
            self.pass1Result.append(self.p.currentInstruction)
            
    def pass2(self):
        while self.p.hasMoreLines():
            self.p.advance()
            # if self.p.currentInstruction == None:
            #     continue
            if self.p.instructionType() == 'A_INSTRUCTION':
                if not (self.p.currentInstruction[1] in self.digitTable):
                    if self.p.symbol() in self.st.SymbolTable:
                        self.p.currentInstruction = '@' + str(self.st.SymbolTable[self.p.symbol()])
                    else: 
                        self.st.addEntry(self.p.symbol(), str(self.st.varNum))
                        self.st.varNum += 1
                        self.p.currentInstruction = '@' + self.st.SymbolTable[self.p.symbol()]
            self.pass2Result.append(self.p.currentInstruction)
            
    def pass3(self):
        while self.p.hasMoreLines():
            self.p.advance()
            if self.p.instructionType() == 'A_INSTRUCTION':
                address = self.p.symbol()
                tmp = format(int(address), 'b')
                prefix = '0'*(16-len(tmp))
                address = prefix+tmp
                self.p.currentInstruction = address
                
            elif self.p.instructionType() == 'C_INSTRUCTION':
                dest = self.p.dest()
                comp = self.p.comp()
                jump = self.p.jump()
                bcomp, bdest, bjump = '',self.c.dest(''),self.c.jump('')
                if comp != None:
                    bcomp = self.c.comp(comp)
                if dest != None:
                    bdest = self.c.dest(dest)
                if jump != None:
                    bjump = self.c.jump(jump)
                tmp = '111' + bcomp + bdest + bjump
                self.p.currentInstruction = tmp
            else: continue
            self.bin.append(self.p.currentInstruction)
        

if __name__ == "__main__":
    n = sys.argv[1][:-4]
    with open("./"+sys.argv[1], 'r') as f:
        l = f.readlines()
    H = HackAssembler(l)
    with open("./"+n+'.hack', 'w') as f:
        f.writelines(H.bin)