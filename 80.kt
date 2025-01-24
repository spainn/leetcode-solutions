class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var original = 0
        var isTwo: Boolean = false
        var k: Int = 0

        for (i in 1..nums.lastIndex) {

            if ((nums[i] == nums[original]) && (i != original)) {
                nums[original+1] = nums[i]
                isTwo = true

            } else {

                original += if (isTwo) 2 else 1
                nums[original] = nums[i]
                isTwo = false
            }
        }

        original += if (isTwo) 2 else 1
        return original
    }
}
