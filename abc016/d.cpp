#include<vector>
#include<iterator> 
#include<utility>
#include<cmath>
#include<iostream>
#include<cstdlib>
#define INF 2000
#define PTYPE double
using namespace std;

struct Point
{ 
  PTYPE x, y; 
  Point() {}
  Point(PTYPE _x, PTYPE _y) { x = _x; y = _y; } 
  
#define DEFINE_OPERATOR(OP) \
  bool operator OP(const Point& rhs) const { return x OP rhs.x && y OP rhs.y; }
  DEFINE_OPERATOR(==)
  DEFINE_OPERATOR(<)
#undef DEFINE_OPERATOR
};


Point intersection_lines(PTYPE a1, PTYPE b1, PTYPE a2, PTYPE b2)
{
  if(a1 == a2)
    return Point(INF, INF);
  /* y = a1x + b1
   * y = a2x + b2
   * 
   * a1x + b1 = a2x + b2
   * (a1 - a2)x = b2 - b1
   * x = (b2 - b1) / (a1 - a2)
   * y = a1((b2 - b1) / (a1 - a2)) + b1
   */
  return Point((b2 - b1) / (a1 - a2), a1 * ((b2 - b1) / (a1 - a2)) + b1);
}

Point intersection_lines(Point p11, Point p12, Point p21, Point p22)
{
  PTYPE a1 = INF;
  PTYPE a2 = INF;
  if(!(p12.x - p11.x || p21.x - p22.x))
    return Point(INF, INF);
  if(p12.x - p11.x)
    a1 = (p12.y - p11.y) / (p12.x - p11.x); 
  if(p22.x - p21.x)
    a2 = (p22.y - p21.y) / (p22.x - p21.x);
  /*
   * y = ax + b
   * b = y - ax
   */
  auto b1 = p12.y - a1 * p12.x;
  auto b2 = p22.y - a2 * p22.x;
  
  Point p;

  if(a1 == INF)
    p = Point(p12.x, a2 * p12.x + b2);
  else if(a2 == INF)
    p = Point(p22.x, a1 * p22.x + b1);
  else
    p = intersection_lines(a1, b1, a2, b2);

  /*
  cout << a1 << "x + " << b1 << "   " << a2 << "x +" << b2 << endl;
  cout << "(" << p.x << ", " << p.y << ")" << endl;
  cout << (p.x + 0.05 >= max(min(p11.x, p12.x), min(p21.x, p22.x))) << endl;
  cout << (p.x - 0.05 <= min(max(p11.x, p12.x), max(p21.x, p22.x))) << endl;
  cout << (p.y + 0.05 >= max(min(p11.y, p12.y), min(p21.y, p22.y))) << endl;
  cout << (p.y - 0.05 <= min(max(p11.y, p12.y), max(p21.y, p22.y))) << endl;
  
  cout << endl;
  */
  
  if(
    p.x + 0.05 >= max(min(p11.x, p12.x), min(p21.x, p22.x)) &&
    p.x - 0.05 <= min(max(p11.x, p12.x), max(p21.x, p22.x)) &&
    p.y + 0.05 >= max(min(p11.y, p12.y), min(p21.y, p22.y)) &&
    p.y - 0.05 <= min(max(p11.y, p12.y), max(p21.y, p22.y)))
    return p;
  return Point(INF, INF);
}

double f(double v)
{
  int n = 1000;
  return v;
  //return v + rand() % n / double(n * 10000);
}

Point A, B;
int N;
vector<Point> P;

int main()
{
  int x, y;
  cin >> x >> y;
  A = Point(f(x), f(y));
  cin >> x >> y;
  B = Point(f(x), f(y));
  cin >> N;
  for(int i = 0; i < N; i++)
  {
    cin >> x >> y;
    P.push_back(Point(f(x), f(y)));
  }

  int n = 0;
  for(int i = 0; i < N; i++)
  {
    auto p =  intersection_lines(A, B, P[i], P[(i + 1) % N]);
    if(p.x != INF)
      n++;
  }
  cout << 1 + n / 2 << endl;
}
