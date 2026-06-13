# Find all prime numbers between 2 and 100 and display eight primes per line.

#Brute Force Enumeration

count = 0
for num in range(2,101):
    is_prime = True
    for i in range(2,int(num**0.5+1)):
        if num % i ==0:
            is_prime = False
            break

    if is_prime:
            print(num, end="\t")
            count+=1

            if count%8 == 0:
                    print()

# Sieve of Eratosthenes

max_n = 100
is_prime = [True] * (max_n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_n**0.5)+1):
      if is_prime[i]:
            is_prime[i*i: max_n+1: i] = [False]*len(is_prime[i*i: max_n+1: i])

primes = [n for n, flag in enumerate(is_prime) if flag]

count = 0
for p in primes:
            print(p, end="\t")
            count+=1

            if count%8 == 0:
                    print()