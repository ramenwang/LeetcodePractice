class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # my inefficient version

        num1_len, num2_len = len(nums1), len(nums2)

        stop_index = (num1_len + num2_len)/2
        count1 = count2 = switch = 0
        median = []

        while count1 + count2 < stop_index + 0.5:
            # check if at last element
            if count1 == num1_len:
                switch = 1
            elif count2 == num2_len:
                switch = 2

            if switch == 0:
                if nums1[count1] <= nums2[count2]:
                    median.append(nums1[count1])
                    count1 += 1
                else:
                    median.append(nums2[count2])
                    count2 += 1
            elif switch == 1: # last element of nums1
                median.append(nums2[count2])
                count2 += 1
            else: # last element of nums2
                median.append(nums1[count1])
                count1 += 1

        if round(stop_index) == stop_index:
            return (median[-1] + median[-2])/2

        return median[-1]


# efficient solution
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
