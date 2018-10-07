class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenth = len(height) - 1
        start = 0
        end = lenth
        maxArea = min(height[start], height[end]) * lenth

        while(lenth != 0):
            if (height[start] > height[end]):
                end = end - 1
            else:
                start = start + 1
            lenth = end - start
            area = min(height[start], height[end]) * lenth
            maxArea = max(maxArea, area)

        return maxArea
