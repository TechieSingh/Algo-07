#include<iostream>
using namespace std;


void isPrime(int n, int i){
    while(i<=n){
        if(n==2){
            cout<<"Prime number";
            break;
        }
        else if (n%i==0)
        {
            cout<<"Not a prime number";
            break;
        }
        
        else{
            cout<<"Prime number";
            break;
        }
        i++;
    }
}

int main()
{
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    isPrime(n, 2);
     return 0;
}