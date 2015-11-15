#include<iostream>
using namespace std;

int dp[200][200];
int main()
{
  int N;
  string s;
  cin >> N >> s;
  int ans = 0;
  for(int i = 1; i < N; i++)
  {
    for(int y = 0; y < 200; y++)
      for(int x = 0; x < 200; x++)
        dp[y][x] = 0;
    for(int y = 0; y < i; y++)
    {
      for(int x = 0; x < N - i; x++)
      {
        int v = s[x + i] == s[y] ? 1 : 0;
        dp[y + 1][x + 1] = max(dp[y][x] + v, max(dp[y][x + 1], dp[y + 1][x]));
      }
    }
    ans = max(dp[i][N - i], ans);
  }
  cout << N - ans * 2 << endl;
}
