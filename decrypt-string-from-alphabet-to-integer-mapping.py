class Solution:
    def freqAlphabets(self, s: str) -> str:
        import re
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall('\d\d#|\d', s))
