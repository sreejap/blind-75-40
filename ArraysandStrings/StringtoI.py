        # algo- remove white spaces at the beginning, 
        # see if there is a sign letter + or -
        # if starting with digit make the number until we find the next non digit char
        # start from left to right, multiply by 10 the current val each time and then add the next digit
        # check if currsum < max /10 or if currsum == max / 10 and digit is < last digit of max then we add
        # otherwise return max num pos or max sum neg
    #https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        index = 0
        res = 0
        n = len (s)
        MAX_VAL = 2**31
        INT_MAX = MAX_VAL - 1
        INT_MIN = -(MAX_VAL) 
        # handle white spaces before at the beginning
        while index < n and s[index] == " ":
            index += 1
        
        if index < n and s[index] == "+":
            index += 1
            sign = 1
        elif index < n and s[index] == "-":
            index += 1
            sign = -1
        
        while index < n and s[index].isdigit():
            digit = int (s[index])
            if res > INT_MAX // 10 or (res == (INT_MAX //10) and digit > INT_MAX %10 ):
                return INT_MAX if sign == 1 else INT_MIN 

            res = res * 10 + digit
            index += 1
        
        res = res * sign
        return res
        
