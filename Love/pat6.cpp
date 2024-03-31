#include<iostream>
using namespace std;

int main()
{
    int col, row;
    int Star, Space;
    cin>>col;
    row = 1;
    while (row<=col)
    {
        Star = 1;
        Space = 1;
        while (Space<=col-row)
        {
            cout<<"  ";
            Space++;
        }
        while (Star<=2*row-1)
        {
            cout<<"* ";
            Star++;
        }
        
        cout<<endl;
        row++;
    }

     return 0;
}

// 5
//         * 
//       * * * 
//     * * * * * 
//   * * * * * * * 
// * * * * * * * * * 