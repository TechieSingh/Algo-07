#include<iostream>
using namespace std;

int main()
{
    int row;
    cin>>row;
    int col =1;
    int val = 'A';
    while (col<=row)
    {
        int i=1;
        while (i<=row)
        {
            cout<<char(val);
            i++;
        }
        val++;
        col++;
        cout<<endl;
    }
     return 0;
}