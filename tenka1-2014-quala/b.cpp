#include<queue>
#include<string>
#include<utility>
#include<vector>
#include<functional>
#include<iostream>
using namespace std;

int kabu = 5, combo, damage, n;
string s;
bool stop[1001000];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> th, dm, back;
int main()
{
  cin >> s;
  n = s.length();
  for(int i = 0; i < n + 10; i++)
  {
    while(!th.empty() && th.top().first == i)
    {
      dm.push(make_pair(
            th.top().first + 1, 
            (int)(th.top().second * (1 + (combo / 10) * 0.1))));
      th.pop();
    } 
    while(!dm.empty() && dm.top().first == i)  
    {
      damage += dm.top().second;
      dm.pop();
      combo++;
    }
    while(!back.empty() && back.top().first == i)
    {
      kabu += back.top().second;
      back.pop();
    }
    
    if(i >= n || stop[i] || s[i] == '-')
      continue;
    switch(s[i])
    {
      case 'N':
        if(!kabu)
          break;
        th.push(make_pair(i + 1, 10));
        back.push(make_pair(i + 7, 1));
        kabu--;
        break;
      case 'C':
        if(kabu < 3)
          break;
        th.push(make_pair(i + 3, 50)); 
        back.push(make_pair(i + 9, 3));
        stop[i + 1] = stop[i + 2] = false;
        kabu -= 3;
    }
  }
  cout << damage << endl;
}
