#include<iostream>
#include<queue>
#include<vector>
#include<cmath>
using namespace std;

vector<int> edges[100000];
int N;
int nodes[100000][2];
bool done[100000];

int main()
{
  cin >> N;
  for(int i = 0; i < N; i++)
  {
    int a, b;
    cin >> a >> b;
    a--; b--;
    edges[a].push_back(b);
    edges[b].push_back(a);
  }

  queue<int> q;
  q.push(-1);
  q.push(0);
  q.push(0);
  while(!q.empty())
  {
    auto p = q.front(); q.pop();
    auto tt = q.front(); q.pop();
    auto f = q.front(); q.pop();
    if(done[tt])
      continue;
    done[tt] = true;
    nodes[tt][0] = p; 
    nodes[tt][1] = f;
    for(const auto& v : edges[tt])
    {
      if(v == p || done[v])
        continue;
      q.push(tt);
      q.push(v);
      q.push(f + 1);
    }
  }
  for(int i = 0; i < N; i++)
    cout << nodes[i][0] << " ";
  cout << endl;
  for(int i = 0; i < N; i++)
    cout << nodes[i][1] << " ";
  cout << endl;
  int Q;
  cin >> Q;
  int t[2];
  for(int i = 0; i < Q; i++)
  {
    int t[2];
    cin >> t[0] >> t[1];
    int xx = nodes[t[0]][1] > nodes[t[1]][1] ? 1 : 0;
    for(int i = 0; i < abs(nodes[t[0]][1] - nodes[t[1]][1]); i++)
    {
      cout << t[0] << " " << t[1] << endl;
      cout << nodes[t[0]][1] << " " << nodes[t[1]][1] << endl;
      t[xx] = nodes[t[xx]][0];
    }
    cout << t[0] << " " << t[1] << endl;
    while(true)
    {
      if(t[0] == t[1])
      {
        cout << nodes[t[0]][1] * 2 << endl;
        break;
      }
    }
    t[0] = nodes[t[0]][0];
    t[1] = nodes[t[0]][1];
  }
}
