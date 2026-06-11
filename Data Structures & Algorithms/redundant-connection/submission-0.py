class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]

        def find(n):
            return n if parents[n] == n else find(parents[n])

        for p, c in edges:
            pup, cup = find(p), find(c)

            if pup == cup:
                return [p, c]

            parents[pup] = parents[cup]

        