#include<string>
#include<iostream>
using namespace std;

int main()
{
  string s;
  cin >> s;
  if(s.length() == 1)
  {
    cout << 0 << endl;
    return 0;
  }
  cout << s.length() << endl;
  int not_symmetry_count = 0;
  for(int i = 0; i < s.length() / 2; i++)
  {
    if(s[i] != s[s.length() - i - 1])
      not_symmetry_count++;
  }
  
  if(not_symmetry_count != 1)
    cout << 25 * s.length() << endl;
  else
    cout << 25 * s.length() - 2 << endl;
}
