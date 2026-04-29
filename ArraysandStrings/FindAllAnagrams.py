# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# important to get the correct index of left char
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len (s):
            return res
        
        chars_p = Counter (p)
        window_chars = Counter (s[:len(p)]) # to get the firstwindow of len p, len p is excluded here 

        if chars_p == window_chars:
            res.append (0)

        for i in range (len(p),len(s)): # include len p here 
            left_index = i - len(p)
            left_char = s [left_index]

            window_chars [left_char] -= 1
            if window_chars [left_char] == 0:
                del window_chars [left_char]
                
            right_char = s[i]
            window_chars [right_char] += 1

            if chars_p == window_chars:
                res.append (left_index+1)
        return res
