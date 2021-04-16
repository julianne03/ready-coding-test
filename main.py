s = '567'

answer = int(s[0])

for i in range(len(s) - 1) :
  if int(s[i]) <= 1 :
    answer = answer + int(s[i+1])
  else :
    answer = answer * int(s[i+1])

print(answer)
