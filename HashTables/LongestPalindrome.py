# we add to the set if char doesn't exist and when we find a char that exists in the set, we add 2 to the res and remove the char, so the end we would have 1 char remaining which is not matching and we can add that to result
class Solution:
    def longestPalindrome(self, s: str) -> int:
       # t(c)- o(N) 
       # s(c) - o(1) because 52 chars
        char_set = set() # abccccdd
        res = 0
        for c in s:
            if c in char_set:
                res += 2
                char_set.remove(c)
            else:
                char_set.add(c) # adding to set

        if len(char_set)!=0:
            res += 1        
        return res
