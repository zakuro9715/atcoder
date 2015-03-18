#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
  int w, h, ans = 0;
  int c[100][100];
  int m[101][101]; // 累積和を入れるための配列
  cin >> h >> w;
  for(int y = 0; y < h; y++)
  {
    for(int x = 0; x < w; x++)
    {
      cin >> c[y][x];
      c[y][x] *= y % 2 && x % 2 || !(y % 2 || x % 2) ? 1 : -1;
    }
  }

  // 累積和を計算
  for(int y = 1; y <= h; y++)
    for(int x = 1; x <= w; x++)
      m[y][x] = c[y - 1][x - 1] + m[y - 1][x] + m[y][x - 1] - m[y - 1][x - 1];
  
  // 始点を選ぶ
  for(int sy = 0; sy < h; sy++)
  {
    for(int sx = 0; sx < w; sx++)
    {
      // 終点を選ぶ
      for(int ey = sy + 1; ey <= h; ey++)
      {
        for(int ex = sx + 1; ex <= w; ex++)
        {
          if(!(m[ey][ex] - m[ey][sx] - m[sy][ex] + m[sy][sx])) 
            ans = max(ans, (ey - sy) * (ex - sx));
        }
      }
    }
  }
  cout << ans << endl;
}
