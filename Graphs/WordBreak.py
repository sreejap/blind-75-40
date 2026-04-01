# https://leetcode.com/problems/word-break/
# T(C) - o(n^3+m*k) - n is length of s, m is size of dictionary k is average length of the words in dict, mk is time spent to create the set words
# S(C) - o(n+mk)
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        seen = set()

        queue = deque ([0])
        while queue:
            start = queue.popleft()

            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if end in seen:
                    continue

                word = s[start:end] #- T(C) - o(n^2) * O(n) to create substrings
                if word in words:
                    queue.append (end)
                    seen.add(end)
        
        return False
