from Coding.BinaryTree.BST import BST

class PathSum2:

    def pathSum(self, root, sum):
        """
        PathSum with the node data from root to leaf

        Args:
            root: BST root
            sum: target sum
        
        """
        self.array = []
        self.list1 = []
        
        if root is None: 
            return 
        
        self.__hasPathSumHelper(root, sum)
        
        return self.array
    
        
    def __hasPathSumHelper(self, node, remainingSum):
        
        if node is None: 
            return 
        
        self.list1.append(node.data)    
        if remainingSum == node.data and node.leftChild is None and node.rightChild is None: 
            self.array.append(list(self.list1))
        else:
            self.__hasPathSumHelper(node.leftChild, remainingSum - node.data)
            self.__hasPathSumHelper(node.rightChild, remainingSum - node.data)

        self.list1.pop()

if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(4)
    bst.insert(8)
    bst.insert(11)
    bst.insert(13)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)

#                 5
#             4       8
#         3                11
#     2                          13
# 1                               
    sol = PathSum2()
    print(sol.pathSum(bst.root, 15))


            