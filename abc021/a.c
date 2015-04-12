#include<stdio.h>

int a[4];
int main()
{
  int n, i, j = 0;
  scanf("%d", &n);
  for(i = 0; i < 4; i++)
  {
    if((1 << i) & n)
    {
      a[0]++;
      a[++j] = 1 << i;
    }
  }
  printf("%d\n", a[0]);
  for(i = 0; i < a[0]; i++)
    printf("%d\n", a[i + 1]);
}
