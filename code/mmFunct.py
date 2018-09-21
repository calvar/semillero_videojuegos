

def printConfig(config):
    """Print the configuration"""
    for i in range(3):
        for j in range(3):
            print(config[i][j]," ",end="")
        print()

        
def win(config):
    """Recieve a tic-tac-toe board configuration.
    Return if a symbol has won the match, and the symbol"""
    test1 = config[0][0]==config[1][1] and config[1][1]==config[2][2]
    if test1:
        if config[0][0] == 'x':
            return (True, 'x')
        elif config[0][0] == 'o':
            return (True, 'o')
    test2 = config[0][2]==config[1][1] and config[1][1]==config[2][0]
    if test2:
        if config[0][2] == 'x':
            return (True, 'x')
        elif config[0][2] == 'o':
            return (True, 'o')
    for i in range(3):
        test3 = (config[i][0]==config[i][1] and config[i][1]==config[i][2])
        if test3:
            if config[i][0] == 'x':
                return (True, 'x')
            elif config[i][0] == 'o':
                return (True, 'o')
        test4 = (config[0][i]==config[1][i] and config[1][i]==config[2][i])
        if test4:
            if config[0][i] == 'x':
                return (True, 'x')
            elif config[0][i] == 'o':
                return (True, 'o')
    return (False,'-')


def nextConfig(config, symb):
    """Recieve a configuration and return a list with all the
    possible configurations in the next move using symbol symb"""
    available = []
    for i in range(3):
        for j in range(3):
            if config[i][j] == '-':
                available.append([i,j])
    newConf = []
    for a in available:
        nc = [[],[],[]]
        for i in range(3):
            nc[i] = [j for j in config[i]]
        nc[a[0]][a[1]] = symb
        newConf.append(nc)
    return newConf


def minmax(myTree):
    #print("pointers: ",myTree.pointers)
    if  len(myTree.pointers) == 0:
        #print("esta es una hoja y su puntaje es {}".format(myTree.score))
        return myTree.score
    else:
        #print("esta no es una hoja voy a recursion!")
        aux = []
        for t in myTree.pointers:
            aux.append(minmax(t))
        #print("scores: ",aux)
        #return max(aux)
             
        if myTree.currentSymb == 'o':
#            print(minmax(myTree.pointers[0].score))
            return max(aux) 
        else:
            return min(aux)
