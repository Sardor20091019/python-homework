
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def digit_sum(k):
    return sum(map(int, str(abs(k))))


def print_powers_of_two(N):
    res = []
    power = 2
    while power <= N:
        res.append(power)
        power *= 2
    print(' '.join(map(str, res)))


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))



evens = list(filter(lambda x: x % 2 == 0, numbers))
