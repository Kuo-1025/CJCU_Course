#include <iostream>

using namespace std;

void myFunction(string fname) {
    cout << fname << " Doe\n";
}

int main() {
    myFunction("John");
    // Output : John Doe
    
    return 0;
}