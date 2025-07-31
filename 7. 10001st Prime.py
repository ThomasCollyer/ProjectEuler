primes = [2]
current_num = 2

while len(primes) < 10001:
    current_num += 1
    prime_flag=1
    for prime in primes:
        if current_num % prime == 0:
            prime_flag = 0
            break
    if prime_flag ==1:
        primes.append(current_num)


print(primes[-1])
