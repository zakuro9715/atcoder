#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int N, K, M, A[50][1000], B[50];
bool D[1000000];

int getk(int k, int j)
{
  return K / N + (j < K % N ? 1 : 0);
}

int main()
{
  cin >> N >> K;
  for(int i = 0; i < N; i++)
    for(int j = 0; j < K; j++)
      cin >> A[i][j];
  M = K;
  for(int i = 0; i < N; i++)
  {
    vector<int> p;
    bool flag = true;
    while(flag)
    {
      flag = false;
      for(int j = 0; j <= i; j++)
      {
        for(int k = B[j]; k < getk(K, j); k++)
        {
          if(D[A[j][k]])
          {
            flag = true;
            K++;
          }
          else
          {
            p.push_back(A[j][k]);
            D[A[j][k]] = true;
            M--;
            if(!M)
              goto end;
          }
        }
        B[j] = getk(K, j);
      }
    }
end:
    if(p.size() == 0)
      cout << endl;
    else
    {
      sort(p.begin(), p.end());
      for(int i = 0; i < p.size() - 1; i++)
        cout << p[i] << " ";
      cout << p[p.size() - 1] << endl;
    }
    if(!M)
      return 0;
  }
}
