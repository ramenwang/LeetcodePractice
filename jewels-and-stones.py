class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(S)>50 or len(J)>50:
            return
        count = 0
        for j in J:
            count += sum([j == s for s in S])
        return count
