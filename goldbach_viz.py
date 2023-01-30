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
    if n % 2 or n <= 2:
        raise ValueError("n must be even greater than 2")

    m = n//2

    for i in range(m-1):
        if is_prime(m-i) and is_prime(m+i):
            return m-i, m+i  # obs: p1 y p2 no tiene por qué ser únicos. Me estoy quedando con el primero que encuentro.

    return None


def nested_radii(n, max_depth=0):
    primes = goldbach(n)

    radii = [primes[1] - primes[0]]

    for i in range(max_depth):
        try:
            primes = goldbach(radii[-1])

        except ValueError:
            return radii

        radii.append(primes[1] - primes[0])

    return radii

###################

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    some_evens = range(2000, 2050, 2)

    # obs, sí p1 + p2 = 2n --> p2 - p1 = 2n - 2p1 = 2(n - p1) (i.e. p2 - p1 es par)

    # goldbach_radii = []
    #
    # for n in some_evens:
    #     p1, p2 = goldbach(n)
    #
    #     goldbach_radii.append((n, p2 - p1))

    # plt.plot(some_evens, [g[1] for g in goldbach_radii], '.-')
    # plt.ylabel("p2 - p1")
    # plt.xlabel("2n")

########################

    radii = [nested_radii(n, max_depth=3) for n in some_evens]

    max_depth = max([len(x) for x in radii])

    for i in range(len(radii)):
        radii[i].extend([None]*(max_depth - len(radii[i])))  # completar missing depth con None

    for depth in range(max_depth):
        plt.plot(some_evens, [x[depth] for x in radii], '.-', label = "Depth = " + str(depth))

    plt.legend()
    plt.ylabel("Radius")
    plt.xlabel("2n")