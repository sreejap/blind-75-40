# https://leetcode.com/problems/word-break/
# T(C) - o(n^3+m*k) - n is length of s, m is size of dictionary k is average length of the words in dict, mk is time spent to create the set words
# S(C) - o(n+mk)
# approach - We treat the string like a graph where each index is a node. We start BFS from index 0. For each index in the queue, we try all possible substrings from that index to every possible end index. 
# If a substring is in the dictionary and we haven’t visited that end index before, we add that end index to the queue. This means we’ve found a valid word and now want to check if the rest of the string from that position can also be segmented.
# If we ever reach the end of the string (index == len(s)), we return True because we found a valid segmentation. If the queue becomes empty and we never reach the end, we return False.

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
