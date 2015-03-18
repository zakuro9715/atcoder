def sp(s)
  l, x, n = [], s[0], 0
  s.each_char do |c|
    unless c == x
      l << "#{x}#{n}" 
      x = c
      n = 0
    end
    n += 1
  end
  l
end

puts sp(gets).join
