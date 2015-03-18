#include<iostream>
#include<algorithm>
using namespace std;
 
int N, T[301][2], dp[301][301][301];
 
int dfs(int n, int a, int b)
{
  if(a == 0)
    return 0;
  if(n == N)
    return 0;
 
  if(dp[n][a][b] != -1)
    return dp[n][a][b];
 
  int bb = T[n][0] - 1;
  int aa = 1;
  if(bb > b)
  {
    aa += bb - b;
    bb = b;
  }
  // トッピングが買えない時
  if(aa > a)
    return dp[n][a][b] = dfs(n + 1, a, b);
  // トッピングが買える
  return dp[n][a][b] = max(
      dfs(n + 1, a, b), // 買わない
      dfs(n + 1, a - aa, b - bb) + T[n][1] // 買う
  );  
}
 
int main()
{
  for(int i = 0; i < 301; i++)
    for(int j = 0; j < 301; j++)
      for(int k = 0; k < 301; k++)
        dp[i][j][k] = -1;
  int x, y;
  cin >> x >> y >> N;
  for(int i = 0; i < N; i++)
    cin >> T[i][0] >> T[i][1];
  cout << dfs(0, x, y) << endl;
}
