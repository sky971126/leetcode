#include <iostream>
#include <thread>

void hello(){
    int a = 0;
    for (int i=0;i<100000;i++){
        a = i ^ 2;
    }
    std::cout<<"Hello Concurrent World\n";
}
void do_something(){
    std::cout<<"do something\n";
}
void do_something_else(){
    std::cout<<"do something else\n";
}

class background_task
{
public:
void operator()() const
{
do_something();
do_something_else();
}
};
using namespace std;
int main(){
    std::thread t1(hello);
    //t1.join();
    background_task f;
    t1.join();
    std::thread t2(f);
    std::cout<<"why\n";
    t2.join();
    //f();
    return 0;
}