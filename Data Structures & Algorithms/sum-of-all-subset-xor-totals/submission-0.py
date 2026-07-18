class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for r in range(len(nums)+1):
            for subset in combinations(nums, r ):
                # sum each subset 
                total += self.xor_sum(subset)
        return total

    
    def xor_sum (self,subset):
        xor_total = 0
        for s in subset:
            xor_total ^=s
        return xor_total

        