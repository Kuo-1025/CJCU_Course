#include <iostream>

using namespace std;

class myClass {
    public:
        int myNum;
};

int main() {
    myClass myObj;

    myObj.myNum = 15;
    cout << myObj.myNum << '\n';
    // Output : 15

    return 0;
}