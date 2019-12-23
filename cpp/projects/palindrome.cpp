# include <iostream>
using namespace std;
int main(){
    int a = 2155512;
    int temp = a;
    int res = 0;
    while (a > 0){
        int remainder = a % 10;
        res = res * 10 + remainder;
        a = a / 10;
    }
    cout << bool(temp == res) <<endl;
}