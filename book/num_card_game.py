n = 3
m = 3

result = 0

for i in range(n) :
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)