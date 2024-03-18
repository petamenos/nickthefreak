//ypologismos ginomenou triwn arithmwn

#include <iostream>
using namespace std;
int ginomenou(int a, int b, int c)
{
    int ginomeno;
    ginomeno = a*b*c;
    return ginomeno;
}
int main()
{
    int a;
    int b;
    int c;
    int ginomeno;
    cout<<"dwse enan arithmo"<<endl;
    cin>>a;
    cout<<"dwse akoma enan"<<endl;
    cin>>b;
    cout<<"dwse akoma enan"<<endl;
    cin>>c;
    
    
    ginomeno = ginomenou(a, b, c);
    
    cout<< "to ginomeno einai: "<<ginomeno<<endl;
    return 0;
}

