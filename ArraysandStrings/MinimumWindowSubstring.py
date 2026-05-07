# https://leetcode.com/problems/minimum-window-substring/
# Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T.
# In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. ∣T∣ represents the length of string T.
# Space Complexity: O(∣S∣+∣T∣). ∣S∣ when the window size is equal to the entire string S. ∣T∣ when T has all unique characters.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter (t)
        required = len (dict_t)
        l,r = 0,0 # init the pointers

        formed = 0 # to keep track of how many unique chars with desired frequ are in the window 

        window_counts = {} # create a dict for the current window
        ans = float("inf"), None, None # tuple of the form length, left, right
        while r < len(s):

            character = s[r] # get right char
            window_counts [character] = window_counts.get(character,0) + 1

            if character in dict_t and window_counts[character] == dict_t [character]:
                formed += 1 # we found the freq for the char
            
            while l <=r and formed == required: # we can play with the window once we have the required chars
                # we can slide the window
                character = s[l]

                if r-l+1 < ans[0]: # update the window
                    ans = (r-l+1, l,r)

                window_counts [character] -= 1 # remove the left char

                if character in dict_t and window_counts [character] < dict_t[character]:
                    formed -= 1 # we lost one of the required chars
                
                l += 1 # shrink the window
            
            r += 1 # expand the window

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
