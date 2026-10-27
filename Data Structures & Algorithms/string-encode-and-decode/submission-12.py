class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join("💩" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split("💩")[1:]