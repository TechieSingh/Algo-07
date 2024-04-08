#include<iostream>
using namespace std;

int ncr(int n, int r)
{

    return(n==r || r==0)?1:ncr(n-1,r-1)+ncr(n-1,r);

}

int main()
{
    int n,r;
    cout<<"Enter the value of n and r ";
    cin>>n>>r;
    cout<<ncr(n,r);
     return 0;
}