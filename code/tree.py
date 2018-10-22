import mmFunct as mf

class Tree:
    def __init__(self, lev, maxLev, symb, conf):
        self.level = lev
        self.maxLevel = maxLev
        self.currentSymb = symb
        self.config = conf
        self.score = 0
        self.pointers = []
        
    def printBranch(self):
        print("level= ",self.level)
        print("symbol= ",self.currentSymb)
        mf.printConfig(self.config)
        print("score= ",self.score)
        print()
        
    def addPointers(self, begin):
        mySymb = 'x'
        if not begin:
            mySymb = 'o'
        s = 'o' if self.currentSymb == 'x' else 'x'
        lev1 = self.level + 1
        if (lev1 <= self.maxLevel):
            newC = mf.nextConfig(self.config, s)
            for c in newC:
                self.pointers.append(Tree(lev1,self.maxLevel,s,c))
                
            for t in self.pointers:
                if not mf.win(t.config)[0]:
                    t.addPointers(begin)
                    if lev1 == 9:
                        t.score = 1
                else:
                    if mf.win(t.config)[1] == mySymb:
                        t.score = 2
                        

    def getPointers(self, nvec):
        if len(nvec) <= self.maxLevel:
            comm = ""
            for i in nvec:
                comm += ".pointers[{0}]".format(i)
            return eval("self"+comm)
        else:
            print("{0} is grater than the tree level.".format(len(nvec)))
            return
