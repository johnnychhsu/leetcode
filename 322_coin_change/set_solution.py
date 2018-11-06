class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        totals = {0}
        seen = set()
        for n in itertools.count(0):
            if amount in totals:
                return n
            if not len(totals):
                return -1
            seen |= totals
            totals = {x+y for x in totals for y in coins if x+y <= amount and x+y not in seen}
