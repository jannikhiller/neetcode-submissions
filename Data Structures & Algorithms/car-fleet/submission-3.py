class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        last_time = -1
        in_order = sorted(zip(position, speed), reverse=True)
        for (p, s) in in_order:
            t = (target - p) / s
            if t > last_time:
                last_time = t
                fleets += 1
        return fleets
        