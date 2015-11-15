#include<iostream>
using namespace std;
constexpr int NN = 100010;
int n, s[100000], t[100000];
int x[NN];
int main()
{
  cin >> n;
  for(int i = 0; i < n; i++)
  {
    cin >> s[i] >> t[i];
    x[s[i]]++;
    x[t[i]]--;
  }
  for(int i = 1; i < NN; i++)
  {
    x[i] = x[i - 1] + x[i];
  }
  int st = 0, en = 0;
  int mx = -1;
  for(int i = 0; i < NN; i++)
  {
    if(x[i] > mx)
    {
      st = i;
      mx = x[i];
    }
    if(i > 0 && x[i - 1] == mx && x[i] < mx)
      en = i;
  }
  bool found = false;
  for(int i = 0; i < n; i++)
  {
    if(s[i] <= st && t[i] >= en)
    {
      found = true;
      break;
    }
  }
  cout << mx - (found ? 1 : 0) << endl;
}
