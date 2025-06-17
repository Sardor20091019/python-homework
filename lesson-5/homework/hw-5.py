def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 2. Conditional Statements Exercise
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


# 3. Find even numbers between two numbers without using loop

# Solution 1: With if-else
def even_numbers_with_if(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start <= end:
        print(list(range(start, end + 1, 2)))
    else:
        print([])

# Solution 2: Without if-else (uses max and min and slicing trick)
def even_numbers_no_if(a, b):
    start = a + (a % 2)
    end = b - (b % 2) + 1
    print(list(range(start, end, 2)) if start <= b else [])


# ======= Example usage =======

# Test 1: Leap year check
print("Leap Year Test:", is_leap(2024))  # True

# Test 2: Conditional Statement
check_weird(3)  # Weird
check_weird(4)  # Not Weird

# Test 3: Even number finding
even_numbers_with_if(3, 12)     # [4, 6, 8, 10, 12]
even_numbers_no_if(3, 12)       # [4, 6, 8, 10, 12]
