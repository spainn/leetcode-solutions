class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) > len(t):
            return False

        s_pointer = 0

        for t_pointer in range(len(t)):

            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1

                if s_pointer == len(s):
                    return True

        return False
