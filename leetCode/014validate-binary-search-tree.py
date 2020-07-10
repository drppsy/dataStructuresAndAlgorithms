class TreeNode:

    def __init__(self,x):
        self.val = x
        self.left,self.right = None,None


class Solutions:

    def isValidBST1(self,root):
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)