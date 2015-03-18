#include<iostream>
using namespace std;

int N;

int req(int a, int b)
{
  if(a == b)
    return 0;
  int x;
  cout << "? " << a + 1 << " " << b + 1 << endl;
  cin >> x;
  return x;
}

int f(int s, bool d=false)
{
  int x = 0, xn;
  for(int i = 0; i < N; i++)
  {
    int a = req(i, s);
    if(a > xn)
    {
      x = i;
      xn = a;
    }
  }
  return d ? xn : x;
}

int main()
{
  cin >> N;
  cout << "! " <<  f(f(0), true) << endl;
}
