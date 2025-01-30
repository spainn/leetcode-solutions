class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # python default library solution
        return haystack.find(needle)

        # sliding window solution (probably intended solution)
        # can also use KMP algorithm
        if needle == "":
            return 0

        for l in range(len(haystack) - len(needle) + 1):
            print(haystack[l:l + len(needle)])
            if haystack[l:l + len(needle)] == needle:
                return l

        return -1

