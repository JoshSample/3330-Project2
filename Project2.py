"""
Josh Sample and Jack Thurber
CSCI3330
Project 2
"""
import random
import time


# Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr


# Insertion Sort

# Merge Sort
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


# Quick Sort
def quick_sort(ar):
    # Base case
    if len(ar) <= 1:
        return ar

        # Let us choose middle element a pivot
    else:
        mid = len(ar) // 2
        pivot = ar[mid]

        # key element is used to break the array
        # into 2 halves according to their values
        smaller, greater = [], []

        # Put greater elements in greater list,
        # smaller elements in smaller list. Also,
        # compare positions to decide where to put.
        for indx, val in enumerate(ar):
            if indx != mid:
                if val < pivot:
                    smaller.append(val)
                elif val > pivot:
                    greater.append(val)

                    # If value is same, then considering
                # position to decide the list.
                else:
                    if indx < mid:
                        smaller.append(val)
                    else:
                        greater.append(val)
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


# Driver for sorts
def main():
    # Random lists
    randar1 = [random.randrange(0, 10) for i in range(10)]
    randar2 = [random.randrange(0, 100) for i in range(100)]
    randar3 = [random.randrange(0, 10000) for i in range(10000)]
    randar4 = [random.randrange(0, 1000000) for i in range(1000000)]
    # For bubble sort to have best case, O(n), list needs to be already sorted
    bubble_best = list(range(1, 10000))
    # For bubble sort to have worst case, O(n*n), list should be in reverse order
    bubble_worst = list(reversed(range(1, 10000)))
    # For quick sort to have it's worst case, n*n time, list needs to be sorted
    # thus variable worst_quick will have a sorted list
    worst_quick = list(range(1, 1000000))

    # Bubble Sort Performance
    print("Bubble Sort time: ")
    print("\tRandom List of 10")
    start = time.perf_counter()
    bubble_sort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 100")
    start = time.perf_counter()
    bubble_sort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 10000")
    start = time.perf_counter()
    bubble_sort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tBest case O(n):")
    start = time.perf_counter()
    bubble_sort(bubble_best)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tWorst case O(n*n):")
    start = time.perf_counter()
    bubble_sort(bubble_worst)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")

    # Insertion Sort Performance

    # Merge Sort performance
    print("Merge sort time: ")
    print("\tRandom List of 10")
    start = time.perf_counter()
    merge_sort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 100")
    start = time.perf_counter()
    merge_sort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 10000")
    start = time.perf_counter()
    merge_sort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 1000000")
    start = time.perf_counter()
    merge_sort(randar4)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")

    # Quick Sort performance
    print("Quick sort time: ")
    print("\tRandom List of 10")
    start = time.perf_counter()
    quick_sort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 100")
    start = time.perf_counter()
    quick_sort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 10000")
    start = time.perf_counter()
    quick_sort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tRandom List of 1000000")
    start = time.perf_counter()
    quick_sort(randar4)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\tWorst case O(n*n)")
    start = time.perf_counter()
    quick_sort(worst_quick)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tNote: for optimal worst case pivot should be at the start or end."
          " Pivot for our sort started at the middle.")


if __name__ == "__main__":
    main()
