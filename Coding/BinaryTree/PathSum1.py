from Coding.BinaryTree.BST import BST

def pathSum1(node, target):
    if not node:
        return False
    return __pathSumHelper(node, target)

def __pathSumHelper(node, target):

    #If the node is none then return false
    if not node: 
        return False

    #if the node is leaf and the sum is achieved
    if node.leftChild is None and node.rightChild is None and (node.data == target):
        return True
    
    #remove the node value and check both left and right sides
    return __pathSumHelper(node.leftChild, target - node.data ) or __pathSumHelper(node.rightChild, target - node.data)

if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(4)
    bst.insert(11)

    print(pathSum1(bst.root, 12))