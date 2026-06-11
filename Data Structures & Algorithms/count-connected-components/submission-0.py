class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        count = n
        def find(n):
            if parents[n] == n:
                return n
            return find(parents[n])
        for child, parent in edges:
            childp, parentp = find(child), find(parent)
            if childp == parentp:
                continue
            else:
                parents[childp] = parents[parentp]
                count -= 1

        return count


