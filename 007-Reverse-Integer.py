class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_abs = abs(x)
        rec = 0
        while(x_abs != 0):
            pop = x_abs % 10
            x_abs = x_abs // 10
            rec = rec * 10 + pop

        if not rec < 2147483647:
            return 0
        if x >= 0:
            return rec
        else:
            return -rec

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)