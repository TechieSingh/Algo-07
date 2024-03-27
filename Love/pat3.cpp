#include<iostream>
using namespace std;

int main()
{
    int col;
    cin>>col;
    int row =1;
    while (row<=col)
    {
        int j = 0;
        while(j<=row){
            cout<<row-j<<" ";
            j++;
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
