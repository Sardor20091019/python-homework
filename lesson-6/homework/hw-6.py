from collections import Counter


def insert_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = []
    i = 0
    count = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3 and i != len(txt) - 1:
            
            next_i = i + 1
            if next_i < len(txt) and (txt[next_i] in vowels or (next_i + 1 < len(txt) and txt[next_i + 1] == '_')):
                
                pass
            else:
                result.append('_')
                count = 0
        i += 1
    
    if result and result[-1] == '_':
        result.pop()
    return ''.join(result)


def print_squares(n):
    for i in range(n):
        print(i ** 2)




def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1


def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum is: {total}")


def multiplication_table(num):
    for i in range(1, 11):
        print(num * i)


def display_selected_numbers(numbers):
    for num in numbers:
        if num > 500:
            break
        if num > 150:
            continue
        if num % 5 == 0:
            print(num)


def count_digits(num):
    print(len(str(abs(num))))


def reverse_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


def print_reverse_list(lst):
    for item in reversed(lst):
        print(item)


def print_negative_numbers():
    for i in range(-10, 0):
        print(i)


def print_done():
    for i in range(5):
        print(i)
    print("Done!")


def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)


def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end='  ')
        a, b = b, a + b
    print()


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"{n}! = {result}")


def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for item in (c1 - c2):
        result.extend([item] * (c1[item] - c2.get(item, 0)))
    for item in (c2 - c1):
        result.extend([item] * (c2[item] - c1.get(item, 0)))
    return result
