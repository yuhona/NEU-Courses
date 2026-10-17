class Solution:
    '''
    [left,                               ,right]
     left,    less - 1,|less,    |i   ,greater| greater + 1       right]
     G1: < pivot         G2: = pivot       G3: > pivot
    '''
    def sortArray(self, nums: list[int]) -> list[int]:
        def QuickSort(arr, left, right):
            if left < right:
                less, greater = Partition(arr, left, right)
                QuickSort(arr, left, less - 1)
                QuickSort(arr, greater + 1, right)
        
        def Partition(arr, left, right):
            pivot_idx = random.randint(left, right)
            arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
            x = arr[right]
    # left,    less - 1,|less,          |i   ,greater| greater + 1       right]
    #  G1: < pivot         G2: = pivot                  G3: > pivot
            less, greater = left, right
            i = left # waiting to be checked
            while i <= greater:
                if arr[i] < x:
                    arr[i], arr[less] = arr[less], arr[i]
                    less += 1
                    i += 1
                elif arr[i] > x:
                    arr[i], arr[greater] = arr[greater], arr[i]
                    greater -= 1
                    # no move i
                else:
                    i += 1
            return less, greater
                
        QuickSort(nums, 0, len(nums) - 1)

        return nums