# include <iostream>
# include <unordered_set>
# include <string>
# include <math.h>
using namespace std;

class Solution {
private:
    unordered_set <int> int_set;

public:
    int matrix_add(int p[][3], int size){
        int count = 0;
        int i;
        int j;
        for (auto i=0; i<size; i++){
            for (j=0; j<size; j++){
                count += p[i][j];
            }
        }
        return count;
    }

};

int main(){
    Solution s1;
    const int size = 3;
    int a[size][size] = {{2,3,2},{3,4,8},{9,11,0}};
    int res = s1.matrix_add(a, size);
    string s = "abc";
    cout << s[s.size()-1] << endl;
    int* arr = new int(10);
    arr[0] = 2;
    arr[3] = 5;
    arr[9] = 4;
    //arr[10] = 11;
    char ch = 'a';
    for (auto i=0; i<=15; i++){
        cout << ch++ << '\n';
    } 
    cout << pow(2,3) << endl;
    return 0;
}