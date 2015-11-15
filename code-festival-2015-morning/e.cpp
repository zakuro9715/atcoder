#include<iostream>
#define int long long
using namespace std;
constexpr long long INF = 1000000000000000;
int N;
long long A[10000];

long long dfs(int i, int l, int r)
{
  if(l == r)
    return 0;
  long long ans = INF;
  if(l % 2 == i % 2)
  {
    A[l + 1] += A[l] + 1;
    ans = min(ans, dfs(i + 1, l + 1, r) + A[l]);
    A[l + 1] -= A[l] + 1;
  }
  if(r % 2 == i % 2)
  {
    A[r - 1] += A[r] + 1;
    ans = min(ans, dfs(i + 1, l, r - 1) + A[r]);
    A[r - 1] -= A[r] + 1;
  }
  return ans;
}

signed main()
{
  cin >> N;
  for(int i = 0; i < N; i++)
    cin >> A[i];
  cout << dfs(0, 0, N - 1) << endl;
}
