n = 5 # weights 의 길이
m = 3 # 최대 무게
weights = [1, 3, 2, 3, 2]

counter = [0] * 11

for w in weights :
  counter[w] += 1

result = 0
for i in range(1, m+1) :
  # a가 고를 경우의 수 빼기
  n -= counter[i]
  result += counter[i] * n

print(result)