def preOrder(root):
    if(root):
        print(root.info,end=" ")
        preOrder(root.left)
        preOrder(root.right)
        
 def inOrder(root):
    if(root):
        inOrder(root.left)
        print(root.info,end=" ")
        inOrder(root.right)
        
 def postOrder(root):
   if(root):
        postOrder(root.left)
        postOrder(root.right) 
        print(root.info,end=" ")  
 
 def height(root):
    if root is None:
        return -1
    else:
        lh=height(root.left)
        rh=height(root.right)
        if(lh>rh):
            return lh+1
        else:
            return rh+1
            
  def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1
        
    

