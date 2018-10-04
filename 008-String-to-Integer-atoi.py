class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.lstrip()
        if len(str) == 0:
            return 0

        flagFriChar = ['']
        if str[0] == "-" or str[0] == "+":
            flagFriChar[0] = str[0]
            str = str[1:]

        if len(str) == 0:
            return 0
            
        matchNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
        if str[0] not in matchNum:
           return 0
        
        strNumList = []
        for each in str:
            if each not in matchNum:
                break
            else:
                strNumList.append(each)
        
        intNumList = list(map(lambda x:int(x), strNumList))

        num = 0
        for each in intNumList:
            num = num * 10 + each

        if flagFriChar[0] == '-':
            num = num * -1
        if num > 2147483647:
            return 2147483647
        elif num < -2147483648:
            return -2147483648
        return num

if __name__ == '__main__':
    s = Solution()
    result = s.myAtoi("  -120 id ss")
    print(result)
            