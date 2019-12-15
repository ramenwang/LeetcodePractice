# longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_list = []
        substr_len = 0

        for iChar in s:
            if iChar in substr_list: # check duplication
                # reset substring list from the element next to the duplication
                substr_list = substr_list[substr_list.index(iChar)+1:]

            substr_list.append(iChar)
            substr_len = max(len(substr_list), substr_len)

        return substr_len
