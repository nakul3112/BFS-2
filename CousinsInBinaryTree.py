# Time Complexity (Queue Approach) :
# O(N)

# Space Complexity (Queue Approach) :  
# O(N) , N= No of Nodes



# Approach:
# ==> We can have two approaches. One is Queue based BFS approach and another is DFS approach.
# ==> For Queue approach, we start with creating boolean variables for checking if x and y elements were found.
#     Then initially add the root to the queue, and while queue is not empty: 
# ==> 0) Pop the node from the queue and iterative till number of times qual to lenght of queue:
# ==> 1) If current node popped above has value equal to x or y, then update xFound and yFound accordingly.
# ==> 2) Check if both left and right nodes are equal to x and y, if so they violated "not having same parent" condition
#      so return False right away.
# ==> 3) Else keep adding left and right child nodes(if valid) to the queue
#     of current node popped from the queue, 
# ==> 4) At end of level traversal( "for" loop in Code), if xFound and yFound both are true, then return true, else false.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        xChild = False
        yChild = False

        queue = []
        queue.append(root)

        while(queue):
            qSize = len(queue)
            for i in range(0, qSize):
                # get current Node
                currNode = queue.pop(0)
                if currNode.val == x:
                    xChild = True
                if currNode.val == y:
                    yChild = True
                # chech both child nodes present?
                if currNode.left and currNode.right:
                    if currNode.left.val == x and currNode.right.val == y:
                        return False
                    if currNode.left.val == y and currNode.right.val == x:
                        return False
                
                # else, move on to left and right child nodes(if valid)
                if currNode.left:
                    queue.append(currNode.left)
                
                if currNode.right:
                    queue.append(currNode.right)

            if xChild== True and yChild == True:
                return True

            if xChild== True or yChild == True:
                return False

        return False
