// Provided Instructions:
// Return the number (count) of vowels in the given string.
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.

#include <iostream>
using namespace std;

int getCount(const string& inputStr) {
    int num_vals = 0;
    for (char letter:inputStr) {
        if (string("aeiou").find(letter) != string::npos) num_vals++;
    }
    return num_vals;
}

int main() {
    cout << getCount("abracadabra") << endl;
    return 0;
}

