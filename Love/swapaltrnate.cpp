#include<iostream>
using namespace std;

void swapalternate(int arr[],int size){


    for (int i = 0; i < size; i+=2)
    {
    if (i+1<size)
    {
        swap(arr[i],arr[i+1]);
    }
    }
     for (int i = 0; i < size; i++)
    {
        cout<<arr[i]<<",";
    }

}

int main()
{
    int arr[6]={1,2,3,4,5,6};
    int size = sizeof(arr)/sizeof(arr[1]);
    swapalternate(arr,size);
     return 0;
}