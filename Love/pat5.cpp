#include<iostream>
using namespace std;

int main()
{
    int row, col;
    cin>>col;
    row = 1;
    while (row<=col)
    {
        int val1, val2;
        val1 = 1;
        val2 = col-row-1;
        while (val2>=0)
        {
            cout<<" ";
            val2--;
        }
        while (val1<=row)
        {
            cout<<"*";
            val1++;
        }
       row++;
       cout<<endl;
    }
    
     return 0;
}