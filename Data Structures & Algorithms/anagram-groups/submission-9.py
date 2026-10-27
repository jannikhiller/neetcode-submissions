from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            letter_counts = [0] * 26
            for c in s:
                letter_counts[ord(c) - ord("a")] += 1
            grouped[",".join(str(letter_counts))].append(s)
        return list(grouped.values())