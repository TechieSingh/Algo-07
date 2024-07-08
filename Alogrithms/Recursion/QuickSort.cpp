#include <iostream>
#include <vector>

using namespace std;

// Function to perform partitioning
int partition(vector<int>& arr, int low, int high) {
    // Choose the rightmost element as pivot
    int pivot = arr[high];
    int i = low - 1;  // Pointer for the greater element

    // Traverse through all elements
    for (int j = low; j < high; j++) {
        // If the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot) {
            i++;  // Move the pointer for the greater element
            // Swap the elements at i and j
            swap(arr[i], arr[j]);
        }
    }

    // Swap the pivot element with the element at i+1
    swap(arr[i + 1], arr[high]);

    // Return the partitioning index
    return i + 1;
}

// Function to perform quicksort
void quicksort(vector<int>& arr, int low, int high) {
    // Base case: If the array has one or zero elements, it's already sorted
    if (low < high) {
        // Partition the array and get the pivot index
        int pi = partition(arr, low, high);

        // Recursively apply QuickSort to elements before and after partition
        quicksort(arr, low, pi - 1);  // Sort the elements before the pivot
        quicksort(arr, pi + 1, high); // Sort the elements after the pivot
    }
}

int main() {
    // Test the quicksort function
    vector<int> arr = {3, 6, 8, 10, 1, 2, 1};
    cout << "Original array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    quicksort(arr, 0, arr.size() - 1);

    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
