#include<iostream>
#include<bitset>
using namespace std;

int a[100], N, X, ans;

int main()
{
  cin >> N >> X;
  bitset<100> b(X);
  for(int i = 0; i < N; i++)
    cin >> a[i];
  for(int i = 0; i < N; i++)
    if(b[i])
      ans += a[i];
  cout << ans << endl;
}
