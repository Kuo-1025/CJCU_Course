#include <iostream>

using namespace std;

int main() {
    string food = "Pizza";
    string &meal = food;

    cout << meal << '\n';
    // Output : Pizza

    return 0;
}