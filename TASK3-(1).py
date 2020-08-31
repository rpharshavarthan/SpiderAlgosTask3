# TASK3-(1)
n = input()
digit = list(map(int, n))
sum_oprn = 0
if int(n) < 10:
    print(sum_oprn)
else:
    while True:
        digit_sum = sum(digit)
        digit = list(map(int, str(digit_sum)))
        sum_oprn += 1
        if digit_sum < 10:
            break
    print(sum_oprn)




