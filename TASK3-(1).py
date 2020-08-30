# TASK3-(1)

digit = list(map(int, input()))
sum_oprn = 0
while True:
    digit_sum = sum(digit)
    digit = list(map(int, str(digit_sum)))
    sum_oprn += 1
    if digit_sum < 10:
        break

print(sum_oprn)




