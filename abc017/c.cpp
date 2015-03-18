#include<iostream>
using namespace std;

#define WAN 100001

int N, M, wa[WAN], mem[WAN];

int main()
{
  cin >> N >> M;
  int sum = 0;
  for(int i = 0; i < N; i++)
  {
    int a, b, c;
    cin >> a >> b >> c;
    wa[a - 1] += c;
    wa[b] -= c;
    sum += c;
  }
  int m = wa[0];
  for(int i = 1; i < M; i++)
  {
    wa[i] += wa[i - 1];
    m = min(m, wa[i]);
  }
  cout << sum - m << endl;
}
