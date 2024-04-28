#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
float h,r,t,d,m;
cout<<"Enter Maximum height in meters: \n";
cin>>h;
cout<<"Enter Range in meters:\n";
cin>>r;
m=(atan(4*h/r));
t=m*57.2958;
cout<<"Angle of shot is "<<t<<" degres.\n";
d=sqrt((h*19.6)/(sin(m)*sin(m)));
cout<<"Initial velocity of shot is "<<d*18/5<<" kmph.\n";
return 0;
}


