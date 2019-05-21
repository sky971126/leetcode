#include<iostream>
#include<vector>

using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        std::vector<int> stack1();
        std::vector<int> stack2();
    }
    
    void push(int x) {
        this->stack1().push_back(x);
        if (this->stack1().empty()){
            stack2().push_back(x);
        }
        else{
            back = stack2().back();
            if back < 
        }
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};