#include<queue>
#include<iostream>
#include<vector>
using namespace std;

int N;
vector<int> edge[100000];
bool selected[100000];
int main()
{
  cin >> N;
  for(int i = 0; i < N - 1; i++)
  {
    int a, b;
    cin >> a >> b;
    a--; b--;
    edge[a].push_back(b);
    edge[b].push_back(a);
  }
  priority_queue<int, vector<int>, greater<int>> q;
  q.push(0);
  int cnt = 0;
  while(true)
  {
    int a = q.top(); q.pop();
    cnt++;
    if(cnt == N)
    {
      cout << a + 1 << endl;
      break;
    }
    cout << a + 1 << " "; 
    for(auto v: edge[a])
    {
      if(!selected[v])
      {
        selected[a] = true;
        q.push(v);
      }
    }
  }
}
