class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ftriplets = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                ftriplets.append(triplet)
        res = [0, 0, 0]
        for triplet in ftriplets:
            for i in range(3):
                if triplet[i] == target[i]:
                    res[i] = 1
        return res[0] == res[1] and res[1] == res[2] and res[0] == 1