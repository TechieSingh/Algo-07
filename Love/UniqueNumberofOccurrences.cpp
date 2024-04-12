#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void solution(const vector<int>& arr1) {
    unordered_map<int, int> nums;
    
    for (int num : arr1) {
        nums[num]++;
    }

    for (auto it = nums.begin(); it != nums.end(); ++it) {
    cout << it->first << ": " << it->second << endl;
}

}

int main() {
    vector<int> arr1 = {4, 4, 7, 4, 7, 3};
    solution(arr1);

    return 0;
}
