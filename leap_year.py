import time
import sys

def slow_print(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

time.sleep(0.02)

# --- INTRO ---
slow_print("I am a leap year calculator.")
slow_print("Enter a year:")
slow_print("Let me check it for you...")
slow_print("Please enter an integer number.")
leap_year = input("Enter a year: ")

# --- CHECK IF IT'S A NUMBER ---
try:
    leap_year = int(leap_year)
except:
    slow_print("You did not enter a number. Program stopped.")
    exit()

# --- LOGIC ---
if leap_year % 400 == 0:
    slow_print("1st rule ✅")
    slow_print(f"{leap_year} is a leap year ✅")
elif leap_year % 4 == 0 and leap_year % 100 != 0:
    slow_print("2nd rule: divisible by 4 ✅")
    slow_print(f"{leap_year} is a leap year ✅")
else:
    slow_print(f"{leap_year} is not a leap year ❌")
    slow_print("Because it does not satisfy the rules ❌")
