#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    string hash[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    int a, b;
    cin >> a >> b;
    
    for (int i = a; i <= b; i++)
    {
       if (i < 10)
           cout << hash[i];
       else if (i%2)
           cout << "odd";
       else
           cout << "even";
       cout << '\n';
    }
    return 0;
}
