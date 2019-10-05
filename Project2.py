"""
Josh Sample, Jack Thurber, and Anthony Sweeney
CSCI3330
Project 2
"""
import random
import time


# Bubble Sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    comparison = 0
    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                comparison += 1
                swap(i - 1, i)
                swapped = True

    return arr, comparison


# Insertion Sort
def insertionSort(arr):
    # Start on 2nd element, assume 1st element already sorted
    comparison = 0
    for i in range(1, len(arr)):
        key = arr[i]
        # to keep reference of index of previous element
        j = i - 1
        # moves value up list if larger than value to insert
        while j >= 0 and key < arr[j]:
            # inserts the item
            arr[j + 1] = arr[j]
            j -= 1
        comparison += 1
        arr[j + 1] = key
    # terminate function call promptly
    return arr, comparison


M_COUNTER = 0


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
    global M_COUNTER
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
            M_COUNTER += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            M_COUNTER += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


# Quick Sort
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quick_sort(arr, l, h):
    comparison = 0
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size
    # initialize top of stack
    top = -1
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
            comparison += 1
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
            comparison += 1
    return comparison


# Driver for sorts
def main():
    # Random lists
    # Magnitude increment is 10, 10**2, 10**4, 10**6
    randar1 = [random.randrange(0, 10) for i in range(10)]
    randar2 = [random.randrange(0, 100) for i in range(100)]
    randar3 = [random.randrange(0, 10000) for i in range(10000)]
    randar4 = [random.randrange(0, 1000000) for i in range(1000000)]
    # For bubble sort to have best case, O(n), list needs to be already sorted
    # This is also true for insertion
    bubble_insertion_best = list(range(1, 10000))
    # For bubble sort to have worst case, O(n*n), list should be in reverse order
    # This is also true for insertion
    bubble_insertion_worst = list(reversed(range(1, 10000)))
    # I had to use a global variable to count comparisons in merge sort
    global M_COUNTER
    # For quick sort to have it's worst case, n*n time, list needs to be sorted
    # thus variable worst_quick will have a sorted list
    worst_quick = list(range(1, 10000))

    # Bubble Sort Performance
    print("Bubble Sort:" "\nAverage case O(n*n)")
    print("\tRandom List of 10")
    start = time.perf_counter()
    _, comparison = bubble_sort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 100")
    start = time.perf_counter()
    _, comparison = bubble_sort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 10,000")
    start = time.perf_counter()
    _, comparison = bubble_sort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tBest case O(n) (using list of 10,000):")
    start = time.perf_counter()
    _, comparison = bubble_sort(bubble_insertion_best)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tWorst case O(n*n) (using list of 10,000):")
    start = time.perf_counter()
    _, comparison = bubble_sort(bubble_insertion_worst)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)

    # Insertion Sort Performance
    print("Insertion Sort:" "\nAverage case O(n*n)")
    print("\tRandom List of 10")
    start = time.perf_counter()
    _, comparison = insertionSort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 100")
    start = time.perf_counter()
    _, comparison = insertionSort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 10,000")
    start = time.perf_counter()
    _, comparison = insertionSort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tBest case O(n) (using list of 10,000):")
    start = time.perf_counter()
    _, comparison = insertionSort(bubble_insertion_best)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tWorst case O(n*n) (using list of 10,000):")
    start = time.perf_counter()
    _, comparison = insertionSort(bubble_insertion_worst)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)

    # Merge Sort performance
    print("Merge sort:" "\nAverage case O(n log n)")
    print("\tRandom List of 10")
    start = time.perf_counter()
    merge_sort(randar1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", M_COUNTER)
    M_COUNTER = 0
    print("\tRandom List of 100")
    start = time.perf_counter()
    merge_sort(randar2)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", M_COUNTER)
    M_COUNTER = 0
    print("\tRandom List of 10,000")
    start = time.perf_counter()
    merge_sort(randar3)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", M_COUNTER)
    M_COUNTER = 0
    print("\tRandom List of 1,000,000")
    start = time.perf_counter()
    merge_sort(randar4)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", M_COUNTER)
    print("\tMerge sort always has a time complexity of o(n log n),"
          "so therefor there is no real way to measure best/worse case.")

    # Quick Sort performance
    print("Quick sort:" "\nAverage case O(n log n)")
    print("\tRandom List of 10")
    start = time.perf_counter()
    comparison = quick_sort(randar1, 0, randar1.__len__() - 1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 100")
    start = time.perf_counter()
    comparison = quick_sort(randar2, 0, randar2.__len__() - 1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 10,000")
    start = time.perf_counter()
    comparison = quick_sort(randar3, 0, randar3.__len__() - 1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tRandom List of 1,000,000")
    start = time.perf_counter()
    comparison = quick_sort(randar4, 0, randar4.__len__() - 1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\tWorst case O(n*n) (using list of 10,000)")
    start = time.perf_counter()
    comparison = quick_sort(worst_quick, 0, worst_quick.__len__() - 1)
    end = time.perf_counter()
    print("\t\tTime it took to sort:", end - start, "seconds")
    print("\t\tComparisons:", comparison)
    print("\t\tNote: best time complexity for quick sort is the same as the average case.")


if __name__ == "__main__":
    main()
