module main;
import std.stdio;
import std.array;
import std.string;
import std.conv;
import std.algorithm;

int[][100001] arr;
void main()
{
  int N, C;
  readf("%d %d\n", &N, &C);
  auto s = readln().split().map!(to!int).array;
  foreach(ref a; arr)
    a ~= -1;
  foreach(int i, int c; s)
    arr[c] ~= i;
  foreach(ref a; arr)
    a ~= s.length.to!int();

  for(auto c = 1; c <= C; c++)
  {
    auto a = 0;
    foreach(int i, int v; arr[c][1..$-1])
      a += (v - arr[c][i]) * (s.length - v);
    writeln(a);
  }
}
