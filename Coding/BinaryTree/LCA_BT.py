def lowestCommonAncestor(root, p, q):
    '''
    Returns the lowestCommonAncestor 

    Args: 
        root: BST root node
        p: Node1
        q: Node2

    Returns: 
        Lowest Common Ancestor Node
    '''
    #If the root is None return None
    if not root:
        return None
    #If alteast one value is root then return root
    if root.val == p.val or root.val == q.val:
        return root
    
    #Check left side and right side
    left = lowestCommonAncestor(root.left,p,q)
    right= lowestCommonAncestor(root.right,p,q)

    #If the left side is None then return right
    if not left:
        return right
    #If the right side is None then return left
    if not right:
        return left
    
    #If both are not None then return root
    return root