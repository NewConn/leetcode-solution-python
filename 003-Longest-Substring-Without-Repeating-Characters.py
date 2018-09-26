class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subString = []
        lenth = len(s)
        count = 0
        i = 0
        j = 0

        while(i < lenth and j < lenth):
            if s[j] not in subString:
                subString.append(s[j])
                j = j + 1
                count = max(j - i, count)
            else:
                subString.remove(s[i])
                i = i + 1
        return count