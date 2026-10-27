class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        while l + 1 < r:
            mid = (l+r) // 2
            if sum(-(-p // mid) for p in piles) <= h:
                r = mid
            else:
                l = mid
        return r

        