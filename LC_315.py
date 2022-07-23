# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/

# TC: O(N log N)
# SC: O(N)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]  # record value and index
        result = [0] * n

        def merge_sort(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            merge_sort(arr, low, mid)
            merge_sort(arr, mid + 1, high)
            merge(arr, low, high, mid)

        def merge(arr, low, high, mid):
            m, n = mid - low + 1, high - mid
            left, right = [0] * m, [0] * n
            
            for i in range(m):
                left[i] = arr[low + i]
            
            for j in range(n):
                right[j] = arr[mid + 1 + j]
            
            i, j, k = 0, 0, low
            while i < m and j < n:
                if left[i][0] > right[j][0]:
                    result[left[i][1]] += n - j
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < m:
                arr[k] = left[i]
                i += 1
                k += 1

            while j < n:
                arr[k] = right[j]
                j += 1
                k += 1

        merge_sort(arr, 0, n - 1)

        return result