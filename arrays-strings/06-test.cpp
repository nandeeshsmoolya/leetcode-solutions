#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {3, 7, 2, 9, 4};

    int maximum = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] > maximum) {
            maximum = nums[i];
        }
    }

    cout << maximum;

    return 0;
}