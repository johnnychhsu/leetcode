class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 10:
            if n == 2:
                return 1
            if n == 3:
                return 2
            if n == 4:
                return 4
            if n == 5:
                return 6
            if n == 6:
                return 9
            if n == 7:
                return 12
            if n == 8:
                return 18
            if n == 9:
                return 27
            if n == 10:
                return 36
        else:
            num = n // 3
            res = n % 3
            if res == 0:
                return 3 ** num
            elif res == 1:
                return 3 ** (num-1) * 4
            else:
                return (3 ** num) * res

