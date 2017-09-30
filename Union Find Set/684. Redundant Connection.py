'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ufs = list(range(len(edges)))
        for (x, y) in edges:
            px, py = ufs[x-1], ufs[y-1] 
            while px != ufs[px]: px = ufs[px]
            while py != ufs[py]: py = ufs[py]
            if px == py:
                return (x,y)
            ufs[px] = py
            tx, ty = x-1, y-1
            while ufs[tx] != py: ufs[tx], tx = py, ufs[tx]
            while ufs[ty] != py: ufs[ty], ty = py, ufs[ty]            
                
            

