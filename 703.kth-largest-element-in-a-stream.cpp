/*
 * @lc app=leetcode id=703 lang=cpp
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
#include <iostream>
#include <queue>
#include <vector>
using namespace std;


class KthLargest {
private:
    int k;
    priority_queue <int,vector<int>,greater<int>> pq;
public:
    KthLargest(int k, vector<int>& nums) { 
        this->k = k;
        for (int i=0; i<nums.size(); i++){
            this->add(nums[i]);
        }
    }
    
    int add(int val) {
        if (this->pq.size() < this->k){
            this->pq.push(val);
        }
        else{
            if (this->pq.top() < val){
                this->pq.pop();
                this->pq.push(val);
            }
        }
        return this->pq.top();
    }
};
/*
int main(){
    int arr[] = {4,5,7,2};
    vector<int> v1(arr, arr+4);
    KthLargest k1(3, v1);
    cout << k1.add(9) << endl;
    return 0;
}*/

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
// @lc code=end

