# include <iostream>
# include <unordered_set>
using namespace std;

class Solution {
private:
    unordered_set <int> int_set;

public:
    int distinct(int* p, int size){
        for (int i=0;i<size;i++){
            int_set.insert(p[i]);
        }
        int count = 0;
        for (auto it=int_set.begin(); it!=int_set.end(); it++){
            cout << *it << endl;
            count++;
        }
        return count;
    }

};

int main(){
    Solution s1;
    const int size = 7;
    int a[size] = {2,3,2,3,4,8,9};
    int res = s1.distinct(a, size);
    double b = 3.5;
    const int c = int(b);
    return 0;
}