class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var original = 0
        for (i in nums.indices) {
            var next = i

            if (nums[next] == nums[original]) {
                continue
            } else {
                original += 1
                
                nums[original] = nums[next]

            }
        }

        return original+1
    }
}
