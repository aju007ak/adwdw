
#include <bits/stdc++.h> 
using namespace std; 

set<int> s; 
  

void generateNumber(int count, int a[], int n, 
                    int num, int k) 
{ 
  

  
    if (k == count) { 
      
        s.insert(num); 
        return; 
    } 
  

    for (int i = 0; i < n; i++) { 
        generateNumber(count + 1, a, n, num + a[i], k); 
    } 
} 

void printDistinctIntegers(int k, int a[], int n) 
{ 
    generateNumber(0, a, n, 0, k); 
    cout << "The " << s.size() 
         << " distinct integers are:\n"; 
  
   
    while (!s.empty()) { 
        cout << *s.begin() << " "; 
  
   
        s.erase(*s.begin()); 
    } 
} 

int main() 
{ 
    int a[] = { 3, 8, 17, 5 }; 
    int n = sizeof(a) / sizeof(a[0]); 
    int k = 2; 
  
   
    printDistinctIntegers(k, a, n); 
    return 0; 
} 
