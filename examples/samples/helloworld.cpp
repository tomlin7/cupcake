#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello", "World"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}
