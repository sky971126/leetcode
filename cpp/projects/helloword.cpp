#include <iostream>
#include <vector>
#include <memory>
#include <string>
using namespace std;
int main(){
    // cout << "hello, world!" << endl;
    // vector<float> v1[2];
    // v1[0].push_back(20.1);
    // v1[1].push_back(20);
    // unique_ptr <int> ptr(new int()); 
    // *ptr = 20; 
    // int* ptr1 = new int(25);
    // cout << *ptr << *ptr1; 

    string a = "haoighle";
    string res = "";
    int i = 0;
    while(i < a.size())
    {
        switch (a[i])
        {
            default:
                res += a[i];
                i++;
                cout << i << endl;
                break;
            case 'a':
                i++;
                cout << "a" << i << endl;
                break;
            case 'e':
                i++;
                cout << "e" << i << endl;
                break;
            case 'i':
                i++;
                cout << "i" << i << endl;
                break;
        }
    }
    cout << res << endl;
    return 0;
}