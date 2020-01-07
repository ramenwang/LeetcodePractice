class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit = 0
        for iNum in nums:
            if len(str(iNum)) % 2 == 0:
                even_digit += 1

        return even_digit
