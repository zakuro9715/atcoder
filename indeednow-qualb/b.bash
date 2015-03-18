read s1
read s2
if [ ${#s1} -ne ${#s2} ]; then
  echo -1
  exit
fi
for ((i=0; i < ${#s1}; i++))
do
  f=1
  for ((j=0; j < ${#s1}; j++))
  do
    if [ ${s1:$j:1} != ${s2:$((($i+$j) % ${#s1})):1} ]; then
      f=0
    fi
  done
  if [ $f -eq 1 ]; then
    echo $i
    exit
  fi
done
echo -1
