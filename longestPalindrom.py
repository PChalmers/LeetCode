class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Any palindrome must start with 
        - xx double center
        - xyx singele center
        '''
        # Base cases - empty string and a single char
        if(s == ''):
            return ''
        if(len(s) == 1):
            return s
        # a single char is the lowest accepted palindrome 
        # - mark the first char in case no others are found
        results = {1:(0,0)} 
        # iterate through the string looking for palindromes
        for index in range(len(s)-1):
            # look for double center palindrome
            if(s[index] == s[index+1]):
                offset = 1
                results.update(self.lookForPalindrome(s, index, offset))
            # look for single center palndrome - check the remaining string is long enough
            if(len(s) - index > 2 and s[index] == s[index+2]): # doesn't matter what the center is
                offset = 0
                results.update(self.lookForPalindrome(s, index+1, offset))
        keys = results.keys()
        if(len(keys) < 1): return ''
        result = results[sorted(keys)[-1]] 
        return s[result[0]:result[1]+1] # add 1 as the indexing does not include the last value

    def lookForPalindrome(self, s: str, index: int, offset: int) -> dict:
        temp = 1
        # check there are outter numbers to verify next
        while( (index-temp >= 0) and (index + offset + temp < len(s)) ):
            # Check that the next outter ring of numbers are equal
            if(s[index-temp] == s[index + offset + temp]): 
                temp += 1
            else:
                break
        temp -= 1 # decrease for last check that failed
        size = (index + offset + temp) - (index - temp) + 1 #account for starting point
        return {size: (index - temp, index + offset + temp)}

s = Solution()
print(s.longestPalindrome('')) # 
print(s.longestPalindrome('a')) # a
print(s.longestPalindrome('aa')) # aa
print(s.longestPalindrome('ab')) # 
print(s.longestPalindrome('gfabbafg')) # gfabbafg
print(s.longestPalindrome('gfabbafgjfgjjghdtpgptdh')) # hdtpgptdh
print(s.longestPalindrome('abbabbagfabbafg')) # gfabbafg
print(s.longestPalindrome('babad')) # bab or aba
