def Height(root):
    if root is None:
        return 0
    else:
        return 1 + max(Height(root.left),Height(root.right))

def printGivenLevel(root, level):
    if(root is None):
        return 
    if(level==1):
        print(root.info, end=" ")
    elif(level>1):
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right,level-1) 

def levelOrder(root):
    #Write your code here
    height=Height(root)
    for h in range(1,height+1):
        printGivenLevel(root,h)
