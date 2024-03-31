#include<iostream>
using namespace std;

int subtractProductAndSum(int n) {
        double product,sum;
        sum=0;
        product=1;
        while(n>1){
            n=n%10;
            product=product*n;
            sum=sum+n;
            n=n*0.1;
            cout<<product<<" "<<sum<<endl;
        }
        return product-sum;
    }

int main()
{
    int n;
    cout<<"Enter the number ";
    cin>>n;
    cout<<subtractProductAndSum(n);
     return 0;
}

