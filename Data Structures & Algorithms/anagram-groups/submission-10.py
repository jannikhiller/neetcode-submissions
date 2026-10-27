from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for i, s in enumerate(strs):
            letter_counts = [0] * 26
            for c in s:
                letter_counts[ord(c) - ord("a")] += 1
            grouped[tuple(letter_counts)].append(i)
        return [[strs[i] for i in group] for group in grouped.values()]