import random
import time


# ==========================================
# Merge Sort (adapted from LeetCode 506)
# ==========================================

def merge_sort(arr):
    comparisons = 0

    def sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        arr_left = sort(arr[:mid])
        arr_right = sort(arr[mid:])

        return merge(arr_left, arr_right)

    def merge(L1, L2):
        nonlocal comparisons

        merged = []
        i, j = 0, 0

        while i < len(L1) and j < len(L2):
            comparisons += 1

            if L1[i] <= L2[j]:
                merged.append(L1[i])
                i += 1
            else:
                merged.append(L2[j])
                j += 1

        if i < len(L1):
            merged += L1[i:]

        if j < len(L2):
            merged += L2[j:]

        return merged

    sorted_arr = sort(arr)

    return sorted_arr, comparisons


# ==========================================
# Quick Sort (adapted from LeetCode 912)
# ==========================================

def quick_sort(arr):
    comparisons = 0

    def QuickSort(arr, left, right):
        if left < right:
            less, greater = Partition(arr, left, right)

            QuickSort(arr, left, less - 1)
            QuickSort(arr, greater + 1, right)

    def Partition(arr, left, right):
        nonlocal comparisons

        pivot_idx = random.randint(left, right)
        pivot = arr[pivot_idx]

        less, greater = left, right
        i = left

        while i <= greater:

            comparisons += 1
            if arr[i] < pivot:
                arr[i], arr[less] = arr[less], arr[i]
                less += 1
                i += 1

            else:
                comparisons += 1
                if arr[i] > pivot:
                    arr[i], arr[greater] = arr[greater], arr[i]
                    greater -= 1
                else:
                    i += 1

        return less, greater

    QuickSort(arr, 0, len(arr) - 1)

    return arr, comparisons


# ==========================================
# Experiment
# ==========================================

N = 100000
RUNS = 3

merge_results = []
quick_results = []

for run in range(1, RUNS + 1):

    print(f"\n========== Run {run} ==========")

    # Generate a new random array
    A = [random.randint(0, 1000000) for _ in range(N)]

    # Make copies for a fair comparison
    merge_input = A.copy()
    quick_input = A.copy()

    # Merge Sort
    start = time.perf_counter()
    merge_sorted, merge_comparisons = merge_sort(merge_input)
    merge_time = time.perf_counter() - start

    # Quick Sort
    start = time.perf_counter()
    quick_sorted, quick_comparisons = quick_sort(quick_input)
    quick_time = time.perf_counter() - start

    # Verify correctness
    assert merge_sorted == quick_sorted == sorted(A)

    merge_results.append((merge_comparisons, merge_time))
    quick_results.append((quick_comparisons, quick_time))

    print(
        f"Merge Sort: Comparisons = {merge_comparisons:,}, "
        f"Time = {merge_time:.4f} seconds"
    )

    print(
        f"Quick Sort: Comparisons = {quick_comparisons:,}, "
        f"Time = {quick_time:.4f} seconds"
    )


# ==========================================
# Average Results
# ==========================================

avg_merge_comparisons = sum(x[0] for x in merge_results) / RUNS
avg_merge_time = sum(x[1] for x in merge_results) / RUNS

avg_quick_comparisons = sum(x[0] for x in quick_results) / RUNS
avg_quick_time = sum(x[1] for x in quick_results) / RUNS

print("\n========== Average Results ==========")

print(
    f"Merge Sort: Comparisons = {avg_merge_comparisons:,.0f}, "
    f"Time = {avg_merge_time:.4f} seconds"
)

print(
    f"Quick Sort: Comparisons = {avg_quick_comparisons:,.0f}, "
    f"Time = {avg_quick_time:.4f} seconds"
)


"""

Experimental Results

Run 1:

Merge Sort: 1,536,729 comparisons, 0.1218 seconds

Quick Sort: 3,118,993 comparisons, 0.1441 seconds

Run 2:

Merge Sort: 1,536,050 comparisons, 0.1127 seconds

Quick Sort: 3,076,638 comparisons, 0.1320 seconds

Run 3:

Merge Sort: 1,536,531 comparisons, 0.1147 seconds

Quick Sort: 3,097,334 comparisons, 0.1350 seconds

Average:

Merge Sort: 1,536,437 comparisons, 0.1164 seconds

Quick Sort: 3,097,655 comparisons, 0.1370 seconds

"""