#include <iostream>

using namespace std;

void myFunction() {
    cout << "I just got executed!\n";
}

int main() {
    myFunction();
    myFunction();
    /*
     * Output : 
     * I just got executed!
     * I just got executed!
     */ 

    return 0;
}