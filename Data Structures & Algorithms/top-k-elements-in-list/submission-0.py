from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        item_frequency = Counter(nums)
        return sorted(item_frequency, key=lambda k: item_frequency[k])[-k:]
        