class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums3 = nums1 + nums2
        nums3.sort(reverse = False)
        lenth = len(nums3)
        mid = lenth // 2
        if lenth % 2 == 0:
            midian = (nums3[mid-1] + nums3[mid])/2
        else:
            midian = nums3[mid]
        
        return midian