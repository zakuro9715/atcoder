#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
  int w, h, ans = 0;
  int c[100][100];
  cin >> h >> w;
  for(int y = 0; y < h; y++)
  {
    for(int x = 0; x < w; x++)
      cin >> c[y][x];
  }


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
          int v = 0;
          for(int y = sy; y < ey; y++)
          {
            for(int x = sx; x < ex; x++)
            {
              // ブラックかホワイトかの判定
              bool b = y % 2 && x % 2 || !(y % 2 || x % 2);
              v += c[y][x] * (b ? -1 : 1);
            }
          }
          if(!v)
            ans = max(ans, (ey - sy) * (ex - sx));
        }
      }
    }
  }
  cout << ans << endl;
}
