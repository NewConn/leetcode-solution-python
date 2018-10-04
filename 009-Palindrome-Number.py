class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverNum = 0
        temp = x
        while(temp!=0):
            each = temp % 10
            temp = temp // 10
            reverNum = reverNum * 10 + each

        if reverNum == x:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(121)
    print(result)