#include <iostream>
#include <cstdio>
using namespace std;

int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

int max_of_four(int a, int b, int c, int d) {
    int result = max( max(a,b), max(c,d) );
    return result;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

