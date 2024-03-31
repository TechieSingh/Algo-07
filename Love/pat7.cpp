#include<iostream>
using namespace std;

int main()
{
    int row, col;
    cin>>col;
    row = 1;
    while (row<=col)
    {
        int num1 = 1;
        int star = 1;
        int num = 1;
        while (num<=col-row+1)
        {
            cout<<num<<" ";
            num++;
        }
        while (star<=2*row-2)
        {
            cout<<"* ";
            star++;
        }
        int val=col-row+1;
        while (num1<=col-row+1)
        {
            cout<<(val)<<" ";
            val--;
            num1++;
        }
        row++;
        cout<<endl;
    }
     return 0;
}