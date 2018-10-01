import mmFunct as mf
import tree


#Initialize the tree
maxLev = 9
iniConf = [['-','-','-'],['-','-','-'],['-','-','-']]
iniTree = tree.Tree(0, maxLev, 'o', iniConf)
#add the branches
iniTree.addPointers()

iniTree.score = mf.minmax(iniTree)

# #Win
# p = iniTree.getPointers([0,0,1,1,2])
# p.printBranch()

# #Loose
# p = iniTree.getPointers([0,0,0,1,0,2])
# p.printBranch()

# #Tie
# p = iniTree.getPointers([4,0,4,1,0,2,0,0,0])
# p.printBranch()


# p = iniTree.getPointers([])
# print(p.pointers)
# p.printBranch()

# p = iniTree.getPointers([0,1,0,0,0])
# print(p.pointers)
# p.printBranch()

# p = iniTree.getPointers([0,1,0,0,0,0])
# print(p.pointers)
# p.printBranch()

# p = iniTree.getPointers([0,1,0,0,0,0,0])
# print(p.pointers)
# p.printBranch()

# p = iniTree.getPointers([0,1,0,0,0,0,0,1])
# print(p.pointers)
# p.printBranch()


mf.game(iniTree)
