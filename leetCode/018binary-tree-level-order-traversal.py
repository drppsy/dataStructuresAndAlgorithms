from collections import deque


class TreeNode:

    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solutions:

    def levelOrder(self,root):
        if not root: return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level)
        return result

    def levelOrder2(self,root):
        if not root : return []
        self.result = []
        self._dfs(root,0)
        return self.result

    def _dfs(self,node,level):
        if not node : return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        if node.left : self._dfs(node.left,level+1)
        if node.right: self._dfs(node.right,level+1)