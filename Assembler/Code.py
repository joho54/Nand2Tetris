class Code():
    def __init__(self):
        self.destDic = {'':'000', 'M':'001', 'D':'010', 'DM':'011', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'ADM':'111'}
        self.compDic0 = {'0':'101010', '1':'111111', '-1':'111010', 'D':'001100', 'A':'110000', '!D':'001101', '!A':'110001', '-D':'001111', '-A':'110011', 'D+1':'011111', 'A+1':'110111', 'D-1':'001110', 'A-1':'110010', 'D+A':'000010', 'D-A':'010011', 'A-D':'000111', 'D&A':'000000', 'D|A':'010101'}
        self.compDic1 = {'M':'110000', '!M':'110001', '-M':'110011', 'M+1':'110111', 'M-1':'110010', 'D+M':'000010', 'D-M':'010011', 'M-D':'000111', 'D&M':'000000', 'D|M':'010101'}
        self.jumpDic = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}
        
    def dest(self, s):
        return self.destDic[s]
    
    def comp(self, s):
        if s in self.compDic0:
            return '0'+self.compDic0[s]
        else: return '1'+self.compDic1[s]
    
    def jump(self, s):
        return self.jumpDic[s]
    
if __name__ == '__main__':
    c = Code()
    print(c.dest(''))