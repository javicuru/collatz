def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(n**0.5)

    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True


def goldbach(n):
    assert not n%2 and n > 2, "n must be even greater than 2"

    m = n//2

    for i in range(m-1):
        if is_prime(m-i) and is_prime(m+i):
            return m-i, m+i  # obs: p1 y p2 no tiene por qué ser únicos. Me estoy quedando con el primero que encuentro.

    return None


###################

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    some_ints = range(2, 100)

    goldbach_radii = []

    for n in some_ints:
        p1, p2 = goldbach(2*n)

        goldbach_radii.append((n, n - p1))

    plt.plot(some_ints, [g[1] for g in goldbach_radii])

    plt.ylabel("Goldbach radii")
    plt.xlabel("n")




