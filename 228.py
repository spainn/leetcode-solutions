class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        l, r = 0, 0
        # return the original list if it is empty or only 1 number
        if l >= len(nums) - 1:
            return [str(x) for x in nums]

        while r < len(nums):
            # move to the right one when the next number is one higher than current
            while r+1 < len(nums) and nums[r] + 1 == nums[r+1]:
                r += 1

            # if r == l after moving then append current number to list
            # and increment both pointers
            if r == l:
                output.append(f"{nums[l]}")

            # otherwise append range to list and increment right pointer by one
            # then set new left pointer to right pointer
            else:
                output.append(f"{nums[l]}->{nums[r]}")

            # increment right pointer by 1 then set left pointer equal to right pointer
            r += 1
            l = r
            
        return output

