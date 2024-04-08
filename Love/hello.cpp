#include<iostream>
using namespace std;

void update(int &n)
{
    n++;
}

int main()
{
int n=5;
update(n);
cout<<n<<endl;

     return 0;
}