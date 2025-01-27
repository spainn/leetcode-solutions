class Solution {
    fun majorityElement(nums: IntArray): Int {
        /*
         * Boyer-Moore majority vote algorithm
         */

        var m: Int = 0
        var c: Int = 0

        for (num in nums) {
            if (c == 0) {
                m = num
                c = 1
            } else if (m == num) {
                c += 1
            } else {
                c -= 1
            }

        }

        return m
    }
}
