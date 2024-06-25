if __name__ == 'main':
    x = int(input("Sonni kiriting : "))
    primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, i):
            if j % i == 0:
                is_prime = False
            if is_prime:
                primes.append(j)
    print(*primes)