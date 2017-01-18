#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n = 0;
    cin >> n;
    int input[n];
    
    for (int i = 0; i < n; i++)
        cin >> input[i];

    for (int i = n-1; i >= 0; i--)
        cout << input[i] << ' ';
  
    return 0;
}
