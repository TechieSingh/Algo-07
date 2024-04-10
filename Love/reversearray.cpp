#include<iostream>
using namespace std;

void reverse(int arr[], int size)
{
    int arr2[size];
    for(int i=0; i<size;i++){
        arr2[size-i-1]=arr[i];
    }
        for(int i=0; i<size;i++){
        cout<<arr2[i]<<",";
    }

}

int main()
{
    int arr[5]={12, 92, 13, 4, 75};
    int size= sizeof(arr)/sizeof(arr[0]);
    reverse(arr,size);
     return 0;
}