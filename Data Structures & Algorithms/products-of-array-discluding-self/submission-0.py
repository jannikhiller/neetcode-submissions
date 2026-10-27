import itertools as it

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_partials = it.accumulate(nums, lambda a, b: a*b, initial=1)
        right_partials = list(it.accumulate(reversed(nums), lambda a, b: a*b, initial=1))[::-1]

        return [ l*r for l, r in zip(left_partials, right_partials[1:])]


        # a b c d
        # 1 a ab abc abcd
        # 1 d dc dcb dcba

        # 1*dcb a*dc ab*d abc*1