class TreeNode:

    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solutions:

    def __init__(self):
        self.traversal_path = []

    def preorderTraversal(self,root):
        if root:
            self.traversal_path.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.traversal_path

    def inorderTraversal(self,root):
        if root:
            self.inorderTraversal(root.left)
            self.traversal_path.append(root.val)
            self.inorderTraversal(root.right)
        return self.traversal_path

    def postorderTraversal(self,root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.traversal_path.append(root.val)
        return self.traversal_path

