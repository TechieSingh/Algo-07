#include<iostream>
using namespace std;

void swapalternate(int arr[],int size){

int arr2[size];
    for (int i = 0; i < size; i+=2)
    {
        arr2[i]=arr[i+1];
        arr2[i+1]=arr[i];
    }
        for (int i = 0; i < size; i++)
    {
        cout<<arr2[i]<<",";
    }

}

int main()
{
    int arr[6]={1,2,3,4,5,6};
    int size = sizeof(arr)/sizeof(arr[1]);
    swapalternate(arr,size);
     return 0;
}