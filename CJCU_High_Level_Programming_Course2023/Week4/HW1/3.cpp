#include <iostream>

using namespace std;

int main() {
    string food2 = "Pizza";
    string &ptr = food2;

    cout << &ptr << '\n';
    // Output : 0x62fef0

    return 0;
}