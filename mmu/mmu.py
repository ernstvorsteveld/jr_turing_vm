class MMU:
    def __init__(self):
        self.initMem()
        self.waitForInput = False
    
    def loadMem(self, binProgram):
        if binProgram[0][0] !=  "@":
            self.initMem()
            self.loader = True
        elif binProgram[0][0] ==  "@" and self.loader == False:
            bloader = [('SPEED', 1), ('LIFO', '%_system'), ('JP', '@main')]
            for memVal in bloader:
                self.memory.append(memVal)
            self.loader = True

        for line in binProgram:
            if line[0] == "@":
                info = line.split()
                self.symbolTable[info[0]] = len(self.memory)
                #if len(info) > 1:
                #    self.symbolMap[info[1]] = len(self.memory)
            else:
                self.memory.append(line)
        print(self.memory)


    def initMem(self):
        self.memory = []
        self.virtMemAdresses = {}
        #self.symbolMap ={}
        self.symbolTable = {}
        self.loader = False


    def dumpMem(self):
        return(self.memory)
        
    def readIObuff(self, adres):
        if adres in self.virtMemAdresses.keys():
            memType, memVal = self.memory[self.virtMemAdresses[adres]]
            if memType == "IObuff":
                #memVal_ = memVal.pop()
                return(memVal)
            else:
                return("error: unknow memtype") 
        else:
             return("error: unknow mem adres") 

    def writeIObuff(self, adres, value):
        if adres in self.virtMemAdresses.keys():
            memType, memVal_ = self.memory[self.virtMemAdresses[adres]]
            if memType == "IObuff":
                memVal_.append(int(value))
                self.memory[self.virtMemAdresses[adres]] = (memType, memVal_)
            else:
                return("error: unknow memtype") 
        else:
             return("error: unknow mem adres") 

    def readMem(self, adres):
        if isinstance(adres, int):
            opcode, operand = self.memory[adres]
            if operand != '' and str(operand)[0] == "@":
                operand = self.symbolTable[operand] - adres
            return((opcode, operand)) 
        else:
            if adres in self.virtMemAdresses.keys():
                memType, memVal = self.memory[self.virtMemAdresses[adres]]
                if memType == "MEM":
                    return(memVal)
                if memType == "LIFO":
                    memVal_ = memVal.pop()
                    return(memVal_)
                if memType == "IObuff":
                    if len(memVal) == 0:
                        memVal.append(0)
                        memVal.append(1)
                    memVal_ = memVal.pop(0)
                    return(bin(memVal_)[2:])
                else:
                    return("error: unknow memtype")
            else:
                return("error")

    def writeMem(self, adres, memVal):
        if isinstance(adres, int):
            self.memory[adres] = memVal
        else:      
            if adres in self.virtMemAdresses.keys():
                memType, memVal_ = self.memory[self.virtMemAdresses[adres]]
                if memType == "MEM":
                    self.memory[self.virtMemAdresses[adres]] = (memType, memVal)
                if memType == "LIFO":
                    memVal_.append(memVal)
                    self.memory[self.virtMemAdresses[adres]] = (memType, memVal_)
                if memType == "IObuff":
                    memVal_.append(int(memVal,2))
                    self.memory[self.virtMemAdresses[adres]] = (memType, memVal_)
                else:
                    return("error: unknow memtype")

            if adres not in self.virtMemAdresses.keys() and adres[0] == "$":
                self.virtMemAdresses[adres] = len(self.memory)
                self.memory.append(("MEM", memVal))
            else:
                return("error")
    

    def makeStack(self, memType, adres):
        memVal = []
        if adres not in self.virtMemAdresses.keys() and adres[0] == "%":
            self.virtMemAdresses[adres] = len(self.memory)
            self.memory.append((memType, memVal))
        else:
            self.memory[self.virtMemAdresses[adres]] = (memType, memVal)