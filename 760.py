class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = {val:index for index, val in enumerate(B)}
        return [d[i] for i in A]