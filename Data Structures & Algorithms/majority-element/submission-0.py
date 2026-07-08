class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for i in hashmap.keys():
            if hashmap[i] > n//2:
                return i
        