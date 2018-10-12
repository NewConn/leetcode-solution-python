class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        listNum2Rom = [[]] * 5
        listNum2Rom[0] = []
        listNum2Rom[1] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        listNum2Rom[2] = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C"]
        listNum2Rom[3] = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
        listNum2Rom[4] = ["", "M", "MM", "MMM"]

        listStrNum = list(str(num))
        listRoman = []

        digit = len(listStrNum)
        for i in listStrNum:
            intI = int(i)
            listRoman.append(listNum2Rom[digit][intI])
            digit = digit - 1

        strRoman = ""
        for char in listRoman:
            strRoman = strRoman + char
        return strRoman

if __name__ == '__main__':
    s = Solution()
    result = s.intToRoman(1994)
    print(result)