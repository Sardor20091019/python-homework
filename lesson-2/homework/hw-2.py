import random
import string

# 1. Age Calculator
print("1. Age Calculator")
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year
print(f"{name}, you are {age} years old.\n")

# 2. Extract Car Names from 'LMaasleitbtui'
print("2. Extract Car Names (Text: 'LMaasleitbtui')")
txt1 = 'LMaasleitbtui'
car_names1 = ['Lamborghini', 'Tesla', 'BMW', 'Toyota', 'Ford']
found1 = [car for car in car_names1 if all(c in txt1 for c in car)]
print("Extracted car names:", found1, "\n")

# 3. Extract Car Names from 'MsaatmiazD'
print("3. Extract Car Names (Text: 'MsaatmiazD')")
txt2 = 'MsaatmiazD'
car_names2 = ['Mazda', 'Datsun', 'Ford', 'Honda']
found2 = [car for car in car_names2 if all(c in txt2 for c in car)]
print("Extracted car names:", found2, "\n")

# 4. Extract Residence Area
print("4. Extract Residence Area")
txt3 = "I'am John. I am from London"
area = txt3.split("from")[-1].strip()
print("Residence Area:", area, "\n")

# 5. Reverse String
print("5. Reverse String")
user_string = input("Enter a string to reverse: ")
print("Reversed string:", user_string[::-1], "\n")

# 6. Count Vowels
print("6. Count Vowels")
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count, "\n")

# 7. Find Maximum Value
print("7. Find Maximum Value")
num_list = input("Enter numbers separated by space: ").split()
num_list = [int(n) for n in num_list]
print("Maximum value:", max(num_list), "\n")

# 8. Check Palindrome
print("8. Check Palindrome")
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"'{word}' is a palindrome.\n")
else:
    print(f"'{word}' is not a palindrome.\n")

# 9. Extract Email Domain
print("9. Extract Email Domain")
email = input("Enter your email: ")
domain = email.split('@')[-1]
print("Email domain:", domain, "\n")

# 10. Generate Random Password
print("10. Generate Random Password")
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
