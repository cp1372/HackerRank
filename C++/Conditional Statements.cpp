#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
   int x;
   string hash[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    
   cin >> x;
   if (x < 10)
       cout << hash[x];
   else
       cout << "Greater than 9";
    
   return 0;
}
