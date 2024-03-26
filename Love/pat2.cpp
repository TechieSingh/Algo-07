#include<iostream>
using namespace std;

int main()
{
    int row, col, value;
    cin>>col;
    row =1; 
    while (row <= col)
    {
        int col = 1;
        while (col <= row)
        {
            cout<<row+col-1<<" ";
            col++;
        }
        cout<<endl;
        row++;
    }  
     return 0;
}


/*
Input: 5
Output:
1   
2 3
3 4 5
4 5 6 7
5 6 7 8 9
*/