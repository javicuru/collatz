def collatz_step(x):
    if not x % 2:
        return x/2
    else:
        return 3 * x + 1

def generate_collatz(start, steps=-1):
    a = start

    if steps > 0:
        for n in range(steps):
            a = collatz_step(a)

            yield a


if __name__ == "__main__":
    generator = generate_collatz(801, 100)

    for m in range(80):
        a = next(generator)

        print(a)

        if a == 1:
            break
