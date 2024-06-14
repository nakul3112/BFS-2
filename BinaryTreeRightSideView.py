# Time Complexity (DFS Approach) :
# O(N)

# Space Complexity (DFS Approach):  
# O(H) , H  = Height of tree


# Approach:
# ==> We can have two approaches. One is Queue based BFS approach and another is DFS approach.
# ==> For DFS approach, we start with creating a "result" list and DFS traversal with additional parameter of "level"
#     that keeps track of which depth/level the node lies in.
# ==> Contrary to previous left-first traveral among childs, we first do right recursive calls because
#     we want the right-hand side views. 
# ==> Then if the level of current node becomes equal to lenght of our result list, only then we add it to the result array.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # ===================  Approach 1: Using DFS with level/breadth parameter, TC=>O(n), SC=>O(n) =================== #
    def __init__(self):
        self.result = []

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        self.dfs(root, 0)
        print("Printning the result list here: ", self.result)
        return self.result

    def dfs(self, root, lvl):
        if not root:
            return
        
        # check if the lvl is same as result's length
        if lvl == len(self.result):
            self.result.append(root.val)
        
        # right recursive call
        self.dfs(root.right, lvl + 1)

        # left recursive call
        self.dfs(root.left, lvl + 1)