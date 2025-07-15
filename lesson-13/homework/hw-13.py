from datetime import datetime, timedelta
import re
import pytz
import time

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()
years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
months = today.month - birthdate.month - (today.day < birthdate.day)
if months < 0:
    months += 12
days = (today - birthdate.replace(year=today.year)).days
if days < 0:
    days = (today - birthdate.replace(year=today.year-1)).days
print(f"Your age: {years} years, {months} months, {days} days")


next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_until = (next_birthday - today).days
print(f"Days until next birthday: {days_until}")


current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_str = input("Enter meeting duration (hours:minutes): ")
current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
hours, minutes = map(int, duration_str.split(":"))
end_dt = current_dt + timedelta(hours=hours, minutes=minutes)
print(f"Meeting will end at: {end_dt.strftime('%Y-%m-%d %H:%M')}")


dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz_str = input("Enter your current timezone (e.g., US/Eastern): ")
to_tz_str = input("Enter target timezone (e.g., Asia/Tokyo): ")
dt_naive = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_tz_str)
to_tz = pytz.timezone(to_tz_str)
dt_local = from_tz.localize(dt_naive)
dt_target = dt_local.astimezone(to_tz)
print(f"Converted time: {dt_target.strftime('%Y-%m-%d %H:%M')} ({to_tz_str})")


future_str = input("Enter a future date and time for countdown (YYYY-MM-DD HH:MM:SS): ")
future_dt = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
while True:
    now = datetime.now()
    if now >= future_dt:
        print("Countdown finished!")
        break
    remaining = future_dt - now
    print(f"Time remaining: {remaining}", end='\r')
    time.sleep(1)


email = input("Enter an email address: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")


phone = input("Enter a 10-digit phone number: ")
digits = re.sub(r"\D", "", phone)
if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print(f"Formatted phone number: {formatted}")
else:
    print("Invalid phone number.")


password = input("Enter a password: ")
criteria = [
    len(password) >= 8,
    re.search(r"[A-Z]", password),
    re.search(r"[a-z]", password),
    re.search(r"\d", password)
]
if all(criteria):
    print("Strong password.")
else:
    print("Weak password. Must be at least 8 chars, include uppercase, lowercase, and a digit.")


sample_text = "This is a sample text. This text is for testing word finder."
word = input("Enter a word to find: ")
matches = [m.start() for m in re.finditer(rf"\b{re.escape(word)}\b", sample_text)]
print(f"Occurrences of '{word}': {matches}")


text = input("Enter text to extract dates from: ")
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"
dates = re.findall(date_pattern, text)
print("Dates found:", dates)
 




