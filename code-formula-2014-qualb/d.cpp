#include<iostream>
#define MN 100000
using namespace std;

int coin[MN], coinx[MN], N;
long long dp[MN];

int main()
{
  cin >> N;
  for(int i = 0; i < MN; i++)
  {
    dp[i] = 1;
    if(i < N)
    {
      int x;
      cin >> x;
      coin[i]+= x;
    }
    coin[i + 1] += coin[i] / 10;
    coinx[i] = coin[i] % 10;
    if(coin[i] > 9)
      coin[i] = 9;
  }
  
  long long A = 1, B = 1;
  for(int i = 0; i < MN; i++)
  {
    A = A * (coin[i] + 1);
    B = B * (coinx[i] + 1);
  }
  cout << A + B << endl;;
}
