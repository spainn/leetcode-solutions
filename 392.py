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


# more compact solution using the same principles in a while loop
# removes the need for checking edge cases at the top of the function
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_pointer, t_pointer = 0, 0
        while t_pointer < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == len(s)
