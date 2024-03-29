from collections import deque

class Parser():
    def __init__(self, asm):
        self.asm = deque(asm)
        self.currentInstruction = None

    def hasMoreLines(self):
        return self.asm

    def isComment(self, instruction):
        if len(instruction) >= 2:
            return instruction.startswith('//')
        return False
    
    def advance(self):
        self.currentInstruction = self.asm.popleft()
        if self.isComment(self.currentInstruction) or self.currentInstruction == '':
            self.currentInstruction = None
        
    def instructionType(self):
        if self.currentInstruction[0] == '@':
            return 'A_INSTRUCTION'
        elif self.currentInstruction[0] == '(':
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'

    def symbol(self):   
        if self.instructionType() == 'A_INSTRUCTION':
            return self.currentInstruction[1:]
        if self.instructionType() == 'L_INSTRUCTION':
            return self.currentInstruction[1:-1]

    def dest(self):
        if '=' in self.currentInstruction:
            return self.currentInstruction[:self.currentInstruction.index('=')]
        return
    
    def comp(self):
        if '=' in self.currentInstruction and ';' in self.currentInstruction:
            return self.currentInstruction[self.currentInstruction.index('=')+1:self.currentInstruction.index(';')]
        elif '=' in self.currentInstruction:
            return self.currentInstruction[self.currentInstruction.index('=')+1:]
        elif ';' in self.currentInstruction:
            return self.currentInstruction[:self.currentInstruction.index(';')]
        else:
            return self.currentInstruction
        
    def jump(self):
        if ';' in self.currentInstruction:
            return self.currentInstruction[self.currentInstruction.index(';')+1:]
        return None
            
    
if __name__ == '__main__':
    p = Parser(['comp;jump', '@kill', '(lavel)', '//commt', '@4'])
    while p.hasMoreLines():
        p.advance()
        if p.currentInstruction == None:
            continue
        print(p.instructionType())
        if p.instructionType() == 'A_INSTRUCTION':
            address = p.symbol()
            print('address ',address)
        
