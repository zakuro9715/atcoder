#include<iostream>
#include<map>
using namespace std;

int N, M, aji[5000];

long long dfs(int n, int x)
{
  if(n >= N)
    return 1;
  if(n > N)
    return 0;
  int m = n;
  map<int, int> mem;
  long long res = 0;
  while(m < N && mem.find(aji[m]) == mem.end())
  {
    mem[aji[m]] = m;
    m++;
    res += dfs(m, x + 1);
  }

  return res % 1000000007;
}

int main()
{
  cin >> N >> M;
  for(int i = 0; i < N; i++)
    cin >> aji[i];
  cout << dfs(0, 0) << endl;
}
