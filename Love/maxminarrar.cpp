#include <iostream>
using namespace std;

void maxmin(int arr[], int size) {
    int maxi=INT_MIN;
    int mini=INT_MAX;

    for (int i = 1; i < size; ++i) {
        maxi = max(arr[i], maxi);
        mini = min(arr[i], mini);

    }

    cout << "Maximum: " << maxi << endl;
    cout << "Minimum: " << mini << endl;
}

int main() {
    int array[5] = {12, 92, 13, 4, 75};
    int size = sizeof(array) / sizeof(array[0]);  // Calculate the size of the array
    maxmin(array, size);

    return 0;
}
