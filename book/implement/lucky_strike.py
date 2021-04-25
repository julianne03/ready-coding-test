numbers = input()
num_sum = 0

for i in range(len(numbers) // 2) :
  num_sum += int(numbers[i])

for i in range(len(numbers) // 2, len(numbers)) :
  num_sum -= int(numbers[i])

if num_sum == 0 :
  print('LUCKY')
else :
  print('READY')