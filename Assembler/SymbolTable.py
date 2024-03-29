class SymbolTable():
    def __init__(self) -> None:
        self.SymbolTable = {}
        self.SymbolTable['R0'] = 0
        self.SymbolTable['R1'] = 1
        self.SymbolTable['R2'] = 2
        self.SymbolTable['R3'] = 3
        self.SymbolTable['R4'] = 4
        self.SymbolTable['R5'] = 5
        self.SymbolTable['R6'] = 6
        self.SymbolTable['R7'] = 7
        self.SymbolTable['R8'] = 8
        self.SymbolTable['R9'] = 9
        self.SymbolTable['R10'] = 10
        self.SymbolTable['R11'] = 11
        self.SymbolTable['R12'] = 12
        self.SymbolTable['R13'] = 13
        self.SymbolTable['R14'] = 14
        self.SymbolTable['R15'] = 15
        
        self.SymbolTable['SP'] = 0
        self.SymbolTable['LCL'] = 1
        self.SymbolTable['ARG'] = 2
        self.SymbolTable['THIS'] = 3
        self.SymbolTable['THAT'] = 4
        
        self.SymbolTable['SCREEN'] = 16384
        self.SymbolTable['KBD'] = 24576
        self.varNum = 16
        
    def addEntry(self, symbol: str, address: int):
        #add <symbol, address> onto table
        self.SymbolTable[symbol] = address
        return None
    
    def contains(self, symbol: str):
        #return wheather it contains symbol or not
        return symbol in self.SymbolTable
    
    def getAddress(self, symbol: str):
        #return address connected to symbol
        return self.SymbolTable[symbol]

    
if __name__ == "__main__":
    st = SymbolTable()
    st.addEntry('k', 10)
    print(st.contains('k'))
    print(st.contains('d'))
    print(st.getAddress('k'))
    st.addEntry('d', 10)
    print(st.contains('k'))
    print(st.contains('d'))
    print(st.getAddress('k'))