#include<iostream>
#include<vector>
using namespace std;

#define MV 101
#define P 100
#define ME (MV * MV)
#define INF 1000000000

struct edge
{
  int to, cap, rev;
  edge(int t, int c, int r)
  {
    to = t; cap = c; rev = r;
  }
};

vector<edge> edges[MV];
bool done[MV];
int N, G, E;

int dfs(int v, int t, int f)
{
  if(v == t)
    return f;
 
  done[v] = true;
  for(auto& e: edges[v])
  {
    if(done[e.to] || e.cap <= 0)
      continue;
    auto d = dfs(e.to, t, min(f, e.cap));
    if(d > 0)
    {
      e.cap -= d;
      edges[e.to][e.rev].cap += d;
      return d;
    }
  }
  return 0;
}

void add_edge(int from, int to, int cap)
{
  edges[from].push_back(edge(to, cap, edges[to].size()));
  edges[to].push_back(edge(from, 0, edges[from].size()));
}

int main()
{
  cin >> N >> G >> E;
  for(int i = 0; i < G; i++)
  {
    int p;
    cin >> p;
    add_edge(p, P, 1);  
  }
  for(int i = 0; i < E; i++)
  {
    int a, b;
    cin >> a >> b;
    add_edge(a, b, 1);
    add_edge(b, a, 1);
  }

  int ans = 0;
  while(1)
  {
    fill(done, done + MV, 0);
    auto f = dfs(0, P, INF);
    if(f == 0)
    {
      cout << ans << endl;
      break;
    }
    ans += f;
  }
}
