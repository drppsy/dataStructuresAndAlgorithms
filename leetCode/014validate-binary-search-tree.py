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

    def isValidBST2(self,root):
        self.prev = None
        self.helper(root)

    def helper(self,root):
        if root is None:
            return True

        if not self.helper(root.left):
            return False

        if self.prev and self.prev.val >= root.val:
            return False

        self.prev = root
        return self.helper(root.right)