#include<iostream>
#include<vector>
#include<cmath>
#define INF 1000000000
#define NN (2 << 20)
using namespace std;

vector<int> edges[100000], eu;
int N, Q, e1[100000];

int d[NN * 2];
void update(int i, int v)
{
  i += NN - 1;
  d[i] = v;
  while(i = (i - 1) / 2)
    d[i] = min(d[i * 2 + 1], d[i * 2 + 2]);
}

int query(int a, int b, int i, int l, int r)
{
  if(r <= a || b <= l)
    return INF;
  if(a <= l && r <= b)
    return d[i];
  
  int m = (l + r) / 2;
  return min(query(a, b, i * 2 + 1, l, m), query(a, b, i * 2 + 2, m, r));
}

void dfs(int n, int d, int from)
{
  e1[n] = eu.size();
  for(auto to: edges[n])
  {
    if(to == from)
      continue;
    eu.push_back(d);
    dfs(to, d + 1, n);
  }
  eu.push_back(d);
}

int main()
{
  cin >> N;
  for(int i = 0; i < N - 1; i++)
  {
    int a, b;
    cin >> a >> b;
    a--; b--;
    edges[a].push_back(b);
    edges[b].push_back(a);
  }
  dfs(0, 0, -1);
  for(int i = 0; i < NN * 2; i++)
    d[i] = INF;
  for(int i = 0; i < eu.size(); i++)
    update(i, eu[i]);
  cin >> Q;
  for(int i = 0; i < Q; i++)
  {
    int a, b;
    cin >> a >> b;
    a--; b--;
    int aa = e1[a], bb = e1[b];
    if(aa > bb)
      swap(aa, bb);
    cout << eu[aa] + eu[bb] - query(aa, bb + 1, 0, 0, NN) * 2 + 1 << endl;
  }
}
