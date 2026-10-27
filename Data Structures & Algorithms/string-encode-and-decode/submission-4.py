class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join("," + s.translate({ord(","): "/,", ord("/"): "//"}) for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        escaped = False
        for c in s:
            if escaped:
                result[-1] += c
                escaped = False
                continue
            if c == "/":
                escaped = True
                continue
            if c == ",":
                result.append("")
                continue
            result[-1] += c
        return result
            
