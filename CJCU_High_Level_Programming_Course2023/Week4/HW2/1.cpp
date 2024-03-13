#include <iostream>

using namespace std;

class Item {
    public:
        int weight, price;

        Item(int w, int p): weight(w), price(p) {}

        void print() {
            cout << "The weight of this Item is " << weight << " g.\n";
            cout << "The price of this Item is NT$" << price << ".\n";
        }
};

class Fish: public Item {
    public:
        Fish(int w, int p): Item(w, p) {}
};

class Meat: public Item {
    public:
        Meat(int w, int p): Item(w, p) {}
};

class vegetable: public Item {
    public:
        vegetable(int w, int p): Item(w, p) {}
};

int main() {
    Fish fish1(20, 50);
    Fish fish2(50, 120);

    Meat meat1(10, 90);
    Meat meat2(100, 250);

    vegetable vege1(150, 200);
    vegetable vege2(210, 350);

    string item;

    while (true) {
        cout << "Please enter the Item: ";
        getline(cin, item);

        cout << '\n';

        if (item == "fish1") {
            fish1.print();
        } else if (item == "fish2") {
            fish2.print();
        } else if (item == "meat1") {
            meat1.print();
        } else if (item == "meat2") {
            meat2.print();
        } else if (item == "vege1") {
            vege1.print();
        } else if (item == "vege2") {
            vege2.print();
        } else {
            cout << "Input Error, the Item '" << item << "' doesn't exist\n";
        }

        /*
         * Output :
         * Please enter the Item: fish1
         * 
         * The weight of this Item is 20 g.
         * The price of this Item is NT$50.
         * 
         * Please enter the Item: meat2
         * 
         * The weight of this Item is 100 g.
         * The price of this Item is NT$250.
         * 
         * Please enter the Item: vege2
         * 
         * The weight of this Item is 210 g.
         * The price of this Item is NT$350.
         * 
         * Please enter the Item: I don't Know, H3H3!
         * 
         * Input Error, the Item 'I don't Know, H3H3!' doesn't exist
        */

        cin.ignore();
    }

    return 0;
}