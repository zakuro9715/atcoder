program abc019_a(input, output);
var a, b, c, d: integer;
begin
  read(a); read(b); read(c);
  if a > b then
  begin
    if b > c then
      d := b
    else if a > c then
      d := c
    else
      d := a;
  end
  else
  begin
    if a > c then
      d := a
    else if b > c then
      d := c
    else
      d := b;
  end;
  writeln(d)
end.
