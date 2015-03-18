#include<iostream>
#include<algorithm>
#define INF 1000000000
using namespace std;


int N, M, mem[300][300], l[300], done[300], al = INF, an, mx, d;
int main()
{
  for(int i = 0; i < 300; i++)
    for(int j = 0; j < 300; j++)
      mem[i][j] = INF;
  cin >> N >> M;
  for(int i = 0; i < M; i++)
  {
    int a, b, t;
    cin >> a >> b >> t;
    a--; b--;
    mem[a][b] = mem[b][a] = t;
  }

  for(int s = 0; s < N; s++)
  {
    for(int i = 0; i < 300; i++)
    {
      done[i] = false;
      l[i] = INF;
    }
    l[s] = 0;
    mx = 0;
    while(true)
    {
      d = -1;
      for(int i = 0; i < N; i++)
        if((d == -1 || l[i] < l[d]) && !done[i])
          d = i;
      if(d == -1)
        break;
      done[d] = true;
      for(int i = 0; i < N; i++)
        l[i] = min(l[i], l[d] + mem[d][i]);
      mx = max(mx, l[d]);
    }
    if(mx < al)
    {
      al = mx;
      an = s;
    }
  }
  cout << al << endl;
}
