li = [2, 4, 5, 4, 6]
li.sort()
n = 5
m = 8
k = 3

num_sum = 0

while (True):
    for i in range(k):
        if m == 0:
            break
        num_sum += li[n - 1]
        m = m - 1

    if m == 0:
        break

    num_sum += li[n - 2]
    m = m - 1

print(num_sum)
