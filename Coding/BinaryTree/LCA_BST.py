from Coding.BinaryTree.BST import BST


def lowestCommonAncestor(node, data1, data2):
    '''
    Function to get the lowest common ancestor

    Args: 
        node: BST root node
        data1: First data point 
        data2: Second data point

    Returns: 
        node data of the ancestor
    '''
    if node:
        return __lowestCommonAncestorHelper(node, data1, data2)


def __lowestCommonAncestorHelper(node, data1, data2):
    '''
    Function to get the lowest common ancestor helper for recursion

    Args: 
        node: BST node
        data1: First data point 
        data2: Second data point

    Returns: 
        node data of the ancestor
    '''
    if not node:
        return
    # Check if the data is right side of the root
    if data1 > node.data and data2 > node.data:
        return __lowestCommonAncestorHelper(node.rightChild, data1, data2)
    # Check if the data is left side of the root
    elif data1 < node.data and data2 < node.data:
        return __lowestCommonAncestorHelper(node.leftChild, data1, data2)
    # If the partition happens at the node then retun node
    else:
        return node.data


if __name__ == "__main__":

    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(4)
    bst.insert(11)

    print('Lowest Common Ancestor is {0}'.format(
        lowestCommonAncestor(bst.root, 6, 11)))
