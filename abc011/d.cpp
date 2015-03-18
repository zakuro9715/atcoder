#include<iostream>
#include<map>
#include<iomanip>
using namespace std;

using point = pair<long long, long long>;

int N, D, X, Y, dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
map<point, double> mem[30];
double dfs(int n, long long y, long long x)
{
  if(n == N)
    return x == X && y == Y ? 1.0 : 0.0;
  auto p = make_pair(x, y);
  if(mem[n].find(p) != mem[n].end())
    return mem[n][p];
  double s = 0;
  for(int i = 0; i < 4; i++)
    s += dfs(n + 1, y + dy[i] * D, x + dx[i] * D);
return (mem[n][p] = s / 4.0);
}

int main()
{
  cin >> N >> D >> X >> Y;
  cout << setprecision(15) << dfs(0, 0, 0) << endl;
}
