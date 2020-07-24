#include<sstream>
#include<vector>
#include<iostream>

using namespace std;

vector <int> parseInts(const string& str) {

    vector <int> v;

    stringstream cin(str);
    
    char ch;
    
    int temp;
    
    while(cin >> temp)
    {
        
        v.push_back(temp);
        
        cin >>ch;
    }
    
    return v;
}

int main() {
    
    string str;
    
    cin >> str;
    
    vector<int> integers = parseInts(str);
    
    for(int i = 0; i < integers.size(); i++) {
     
        cout << integers[i] << "\n";
    }

    return 0;
}
