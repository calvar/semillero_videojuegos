import mmFunct as mf
import tree


#Initialize the tree
maxLev = 9
iniConf = [['-','-','-'],['-','-','-'],['-','-','-']]
iniTree = tree.Tree(0, maxLev, 'o', iniConf)
#add the branches
iniTree.addPointers()


# #Win
# p = iniTree.getPointers([0,0,1,1,2])
# p.printBranch()

# #Loose
# p = iniTree.getPointers([0,0,0,1,0,2])
# p.printBranch()

# #Tie
# p = iniTree.getPointers([4,0,4,1,0,2,0,0,0])
# p.printBranch()

iniTree.score = mf.minmax(iniTree)

p = iniTree.getPointers([0,0,0,0,0,0,1])
print(p.pointers)
p.printBranch()

p = iniTree.getPointers([0,0,0,0,0,0,1,1])
print(p.pointers)
p.printBranch()

p = iniTree.getPointers([0,0,0,0,0,0,1,1,0])
p.printBranch()

print(iniTree.score)

#p = iniTree.getPointers([0,0,0,0,0,0,2])
#p.printBranch()

# p = iniTree.getPointers([0,0,1,1,1])
# p.printBranch()

# p = iniTree.getPointers([0,0,1,1,2])
# p.printBranch()

# p = iniTree.getPointers([0,0,1,1,3])
# p.printBranch()

# p = iniTree.getPointers([0,0,1,1,4])
# p.printBranch()
