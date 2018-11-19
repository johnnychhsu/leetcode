class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry < 10:
                digits[i] += carry
                return digits
            else:
                temp = digits[i] + 1
                digits[i] = temp % 10
                carry = temp // 10
        return [1] + digits
