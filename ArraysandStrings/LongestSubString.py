class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr = 0
        char_set = set ()
        left = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
            
            longest_substr = max (longest_substr, i-left+1)
            char_set.add(s[i])

        return longest_substr
