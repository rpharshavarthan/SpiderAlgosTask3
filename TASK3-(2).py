# TASK3-(2)

n = int(input())
m = int(input())
brick_strn = list(map(int, input().split()))
brick_strn.sort()
c, bricks = 0, []
for i in range(m-n+1):
    c += brick_strn[i]
for i in range(m-n+1, m):
    bricks.append(brick_strn[i])
bricks.append(c)
print(min(bricks))


