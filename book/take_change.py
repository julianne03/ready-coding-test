n = 1260
coin_list = [500, 100, 50, 10]
count = 0

for i in coin_list :
  count += n // i
  n = n % i

print(count)