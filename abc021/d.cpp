#include<iostream>
#include<algorithm>
using namespace std;

long long dp[2][100001];
int main()
{
  int n, k;
  cin >> n >> k;
  for(int i = 0; i <= n; i++)
    dp[0][i] = 1;
  for(int i = 1; i <= k; i++)
  {
    dp[i % 2][0] = 0;
    for(int j = 1; j <= n; j++)
      dp[i % 2][j] = (dp[(i + 1) % 2][j] + dp[i % 2][j - 1]) % 1000000007;
  }
  cout << dp[k % 2][n] << endl;
}
