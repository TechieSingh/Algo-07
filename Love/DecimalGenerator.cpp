#include<iostream>
using namespace std;

int main()
{
    int n,i;
    cout<<"Enter the number ";
    cin>>n;
    int ans=0;
    i=0;
    while (n!=0)
    {
        int digit=n%10;
        ans=(digit*pow(2,i))+ans;
        i++;
        n=n/10;
    }
    cout<<ans;

     return 0;
}