class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we want sum(p // k for p in piles) <= h
        l = 0
        r = max(piles)
        while l + 1 < r:
            
            mid = (l+r) // 2
            print(l, r, mid, sum(math.ceil(p / mid) for p in piles))
            if sum(math.ceil(p / mid) for p in piles) <= h:
                r = mid
            else:
                l = mid
        return r

        