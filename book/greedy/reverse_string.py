s = '0001100'

count_zero = 0
count_one = 0

if s[0] == '0' :
  count_zero += 1
else :
  count_one += 1

for i in range(len(s) - 1) :
  if s[i] != s[i+1] :
    if s[i+1] == '0' :
      count_zero += 1
    else :
      count_one += 1

print(min(count_zero, count_one))