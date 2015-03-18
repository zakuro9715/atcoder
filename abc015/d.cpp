#include<iostream>
#include<algorithm>
using namespace std;

#define INF 1000000000
int dp[50][51][10001];
int s[50][2];
int W, N, K;

int dfs(int n, int k, int w)
{
  if(n == N)
    return 0;
  if(dp[n][k][w] != INF)
    return dp[n][k][w];
  int a = dfs(n + 1, k, w);
  if(k < K && w + s[n][0] <= W)
    a = max(a, dfs(n + 1, k + 1, w + s[n][0]) + s[n][1]);
  return dp[n][k][w] = a;
}

int main()
{
  cin >> W >> N >> K;
  for(int i = 0; i < N; i++)
    cin >> s[i][0] >> s[i][1];
  fill((int*)dp, (int*)dp + 50 * 51 * 10001, INF);
  cout << dfs(0, 0, 0) << endl;
}
