#include<stdio.h>

int d[101];
int main()
{
  int N, a, b, p, i, no = 0;
  scanf("%d%d%d", &N, &a, &b);
  scanf("%d", &N);
  d[a] = d[b] = 1;
  for(i = 0; i < N; i++)
  {
    scanf("%d", &p);
    if(d[p])
      no = 1;
    d[p] = 1;
  }
  printf(no ? "NO\n" : "YES\n");
  return 0;
}
