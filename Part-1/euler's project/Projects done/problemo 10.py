N=2000000
s = 0
Primes = [True for k in range(N + 1)]
p = 2
Primes[0] = False  # zero is not a prime number.
Primes[1] = False  # one is also not a prime number.
while  (p * p <= N):
    if Primes[p] == True:
        for j in range(p * p, N + 1, p):
            Primes[j] = False
    p += 1
for i in range(2, N):
    if Primes[i]:
        s += i
print('The sum of prime numbers:', s)
