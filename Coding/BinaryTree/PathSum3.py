from Coding.BinaryTree.BST import BST
class Solution:
    def pathSum3(self, node, target):

        def dfs(node):
            if not node:
                return 
            self.pathSumHelper(node, 0, target)
            dfs(node.leftChild)
            dfs(node.rightChild)
        
        self.count = 0
        dfs(node)
        return self.count

    def pathSumHelper(self, node, sum, target):

        if not node:
            return

        if node.data + sum == target:
            self.count += 1

        self.pathSumHelper(node.leftChild, sum + node.data, target)
        self.pathSumHelper(node.rightChild, sum + node.data, target)

if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(-3)
    bst.insert(3)
    bst.insert(2)
    bst.insert(11)
    bst.insert(3)
    bst.insert(-2)
    bst.insert(1)

    sol = Solution()

    print(sol.pathSum3(bst.root, 8))
