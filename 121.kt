class Solution {
    fun maxProfit(prices: IntArray): Int {

        var l: Int = 0
        var r: Int = 1
        var maxProfit: Int = 0

        while (r < prices.size) {
            if (prices[l] < prices[r]) {
                val profit: Int = prices[r] - prices[l]
                maxProfit = maxOf(profit, maxProfit)
            } else {
                l = r
            }

            r += 1
        
        }

        return maxProfit
    }
}
