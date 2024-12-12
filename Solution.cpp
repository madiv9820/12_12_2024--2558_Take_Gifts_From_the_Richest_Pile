#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        // Create a max-heap using priority_queue to store gift values
        priority_queue<int> pq;
        // Push all gift values into the max-heap
        for(const int& x: gifts) pq.push(x);

        // Perform the gift operation k times
        while(k--) {
            // Pop the maximum gift value from the heap
            int x = pq.top(); pq.pop();
            // Take the square root of the gift value
            x = sqrt(x);
            // Push the transformed gift value back into the heap
            pq.push(x);
        }

        // Initialize a variable to accumulate the remaining gift values
        long long gifts_Left = 0;
        
        // Sum all the remaining gift values
        while(pq.size()) { gifts_Left += pq.top(); pq.pop(); }

        // Return the total value of the remaining gifts
        return gifts_Left;
    }
};

int main() {
    vector<int> gifts = {25,64,9,4,100}; int k = 4;
    Solution sol;
    
    cout << sol.pickGifts(gifts, k) << endl;
}