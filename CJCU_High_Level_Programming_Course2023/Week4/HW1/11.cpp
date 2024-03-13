#include <iostream>

using namespace std;

class myClass {
    public:
        myClass() {
            cout << "Hello, World!\n";
        }
};

int main() {
    myClass myObj;
    // Output : Hello, World!

    return 0;
}