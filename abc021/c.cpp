#include<iostream>
#include<queue>
using namespace std;

long long d[100], N, M, a, b;
bool done[100];
vector<int> g[100];
int main()
{
  cin >> N >> a >> b >> M;
  a--; b--;
  for(int i = 0; i < M; i++)
  {
    int x, y;
    cin >> x >> y;
    x--; y--;
    g[x].push_back(y);
    g[y].push_back(x);
  }
  queue<int>q;
  q.push(a);
  q.push(-1);
  d[a] = done[a] = 1;
  while(q.size())
  {
    int x = q.front(); q.pop();
    if(x == -1)
    {
      if(d[b])
        break;
      continue;
    }
    done[x] = true;
    for(int i = 0; i < g[x].size(); i++)
    {
      int to = g[x][i];
      if(done[to])
        continue;
      if(!d[to])
        q.push(to);
      d[to] = (d[to] + d[x]) % 1000000007;
    }
    q.push(-1);
  }
  cout << d[b] << endl;
}
