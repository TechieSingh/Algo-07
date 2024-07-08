def quicksort(arr, low, high):
    # Base case: If the array has one or zero elements, it's already sorted
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        
        # Recursively apply QuickSort to elements before and after partition
        quicksort(arr, low, pi - 1)  # Sort the elements before the pivot
        quicksort(arr, pi + 1, high) # Sort the elements after the pivot

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1  # Pointer for the greater element
    
    # Traverse through all elements
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Move the pointer for the greater element
            # Swap the elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the partitioning index
    return i + 1

# Test the quicksort function
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
