class Solution:
    def partition(self, s: str):
        res = []

        def is_palindrome(substr):
            substr_len = len(substr)
            is_palin = False
            for c in range(substr_len):
                if substr[c] == substr[substr_len-1]:
                    is_palin = True
                else:
                    is_palin = False
                    break
            return is_palin

        temp_lst = []
        seen = {}
        for i in range(len(s)):
            char = s[i]
            if s[i] in seen:
                next_index = i
                #next_index = s.find(char, i+1)
                # print(next_index)
                # if next_index > 0:
                #check is palindrome
                pali_subs_str = s[seen[s[i]]:next_index+1]
                print(pali_subs_str)
                if is_palindrome(pali_subs_str):
                    res.append([pali_subs_str, s[next_index+1:]])
                    # else:
                    #    for each in pali_sub_str:
                    #        res.append([each])
            seen[s[i]] = i
            temp_lst.append(char)
        res.append(temp_lst)

        return res

# abcabcbb
# aab


sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))
