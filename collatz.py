def collatz_step(x):
    if not x % 2:
        return x/2
    else:
        return 3 * x + 1

def reverse_step(x):
    previous_even = 2 * x
    previous_odd = (x - 1)/3

    if not x % 2 and previous_odd.is_integer():
        return previous_even, int(previous_odd)

    else:
        return previous_even, None

    # if not x % 2:
    #     if previous_odd.is_integer():
    #         return previous_even, previous_odd
    #
    #     else:
    #         return previous_even, None
    #
    # else:
    #     return previous_even, None


def generate_collatz(start, steps=-1):
    a = start

    if steps > 0:
        for n in range(steps):
            a = collatz_step(a)

            yield a

            if a == 1:
                break

def print_collatz_sequence(start, steps=-1):
    generator = generate_collatz(start, steps)

    for num in generator:
        print(num)


if __name__ == "__main__":
    print_collatz_sequence(2, 5)


