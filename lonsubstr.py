class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        str_length = len(s)
        if str_length == 0:
            return 0
        elif str_length == 1:
            return 1
        for x in range(str_length):
            if s[x] in seen:
                start = max(start, seen[s[x]] + 1)
            seen[s[x]] = x
            print(seen)
            max_length = max(max_length, x-start + 1)
            print(s[start:x+1])
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))

# Closures and decorators article:
https: // towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb8
