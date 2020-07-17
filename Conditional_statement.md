#include <bits/stdc++.h>

using namespace std;

int main()
{
    
    int n;
    cin >> n;
    string num[11] ={"Greater than 9","one","two","three","four","five","six","seven","eight","nine","ten"};
    if(n>9){
        cout<<num[0];
    }
    else{
        cout<<num[n];
    }
    return 0;
}
