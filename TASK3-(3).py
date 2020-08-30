# TASK3-(3)

# Finding all prime numbers <= n
n = int(input())
prime = [True for i in range(n + 1)]
prime[0], prime[1] = False, False
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p * 2, n + 1, p):
            prime[i] = False
    p += 1
# Distinct Ci occurs at prime Numbers.
# Counting the number of prime numbers less than or equal to n.
primeNos = prime.count(True)
# Minimum value of sum of all possible distinct values of Ci.
ciSum = (primeNos * (primeNos + 1)) // 2
print(ciSum)
