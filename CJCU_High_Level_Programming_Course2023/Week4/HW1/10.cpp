#include <iostream>

using namespace std;

class myClass {
    public:
        void myMethod() {
            cout << "Hello, World!\n";
        }
};

int main() {
    myClass myObj;

    myObj.myMethod();
    // Output : Hello, World!

    return 0;
}