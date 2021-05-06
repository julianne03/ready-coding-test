count, money = map(int, input().split())
money_list = []

for i in range(count) :
  m = int(input())
  money_list.append(m)

money_list.sort(reverse=True)
answer = 0

for i in range(len(money_list)) :
  if money >= money_list[i] :
    num = money // money_list[i]
    money -= money_list[i] * num
    answer += num
  if money == 0 : break

print(answer)