def is_primes(x):
    for i in range(2, x):
        if (x % i) == 0:
            return
    return x


def get_primes(x, y):
    primes = []
    for i in range(x, y+1):
        if is_primes(i):
            primes.append(i)
    return primes


print(get_primes(11, 25))
