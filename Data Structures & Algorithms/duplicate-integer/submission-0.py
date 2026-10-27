from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(count >= 2 for count in Counter(nums).values())
         