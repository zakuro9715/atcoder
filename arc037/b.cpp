#include<iostream>
#include<vector>
#include<queue>
using namespace std;

typedef pair<int, int> P;

int N, M;
bool g[100][100], done[100];

bool check(int st)
{
  queue<P> q;
  q.push(make_pair(st, -1));
  bool ng = false;
  while(q.size())
  {
    auto p = q.front(); q.pop();
    int n = p.first;
    for(int i = 0; i < N; i++)
    { 
      if(!g[i][n] || i == p.second)
        continue;
      if(done[i])
        ng = true;
      else
      {
        q.push(make_pair(i, n));
        done[i] = true;
      }
    }
  }
  return !ng;
}

int main()
{
  cin >> N >> M;
  for(int i = 0; i < M; i++)
  {
    int a, b;
    cin >> a >> b;
    a--; b--;
    g[a][b] = g[b][a] = true;
  }

  int ans = 0;
  for(int i = 0; i < N; i++)
  {
    if(!done[i] && check(i))
      ans++;
  }
  cout << ans << endl;
}
