#include<iostream>
using namespace std;

int main()
{
    int col;
    cin>>col;
    int row =1;
    while (row<=col)
    {
        int col = 1;
        int value = row;
        while(col<=row){
            cout<<value<<" ";
            value--;
            col++;
        }
        row++;
        cout<<endl;
    }
     return 0;
}

/*
Input: 5
Output:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
*/