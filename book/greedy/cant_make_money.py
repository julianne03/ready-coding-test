n = 5
coins = [3, 2, 1, 1, 9]

coins.sort()

answer = 1
for c in coins :
  if answer < c :
    break
  answer += c

print(answer)