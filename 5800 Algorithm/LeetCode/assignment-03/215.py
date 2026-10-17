class Solution:
    # Randomized Quickselect with Three-Way Partitioning
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def find_kth_largest(arr, left, right, target):
            if left == right:
                return arr[left]

            less, greater = partition(arr, left, right)
            #   [3,2,3,1,2,4,| 5,          5,    | 6 ]
            #idx:0,        5,| 6           7     | 8
            #left,    less-1,|less, |i  ,greater,|greater+1     ,right
            #      < pivot   |=pivot|  unchecked |   > pivot
            if target > greater:
                return find_kth_largest(arr, greater + 1, right, target)

            elif target < less:
                return find_kth_largest(arr, left, less - 1, target)

            else:
                return arr[target]
        
        def partition(arr, left, right):
            pivot_idx = random.randint(left, right)
            pivot = arr[pivot_idx]
            arr[right], arr[pivot_idx] = arr[pivot_idx], arr[right]

            #left,    less-1,|less, |i  ,greater,|greater+1     ,right
            #      < pivot   |=pivot|  unchecked |   > pivot
            less, greater = left, right
            i = left

            while i <= greater:
                if arr[i] < pivot:
                    arr[i], arr[less] = arr[less], arr[i]
                    less += 1
                    i += 1

                elif arr[i] > pivot:
                    arr[i], arr[greater] = arr[greater], arr[i]
                    greater -= 1

                else:
                    i += 1
            return less, greater

        target = len(nums) - k

        return find_kth_largest(nums, 0, len(nums) - 1, target)
