# tracker.py
# Name: Eshtha
# Roll Number: 201730450
# Date: November 2025
# Project: Daily Calorie Tracker CLI Tool

import datetime

print("===========================================")
print("   Welcome to the Daily Calorie Tracker!   ")
print("===========================================")
print("Track your daily meals and monitor calorie intake easily.\n")

# ---------- Task 2: Input & Data Collection ----------
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal name #{i+1}: ")
    calorie_value = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_value)

# ---------- Task 3: Calorie Calculations ----------
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# ---------- Task 4: Exceed Limit Warning System ----------
if total_calories > daily_limit:
    status_msg = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_msg = "✅ You are within your daily calorie limit. Great job!"

# ---------- Task 5: Neatly Formatted Output ----------
print("\n===========================================")
print("           Daily Calorie Summary")
print("===========================================")
print(f"{'Meal Name':<15}{'Calories'}")
print("-------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<15}{calories[i]}")

print("-------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print(status_msg)
print("===========================================\n")

# ---------- Task 6 (Bonus): Save Session Log to File ----------
save = input("Do you want to save this session to a file? (yes/no): ").strip().lower()

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log.txt"

    with open(filename, "w") as file:
        file.write("==== Daily Calorie Tracker Log ====\n")  
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories'}\n")
        file.write("-----------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}{calories[i]}\n")
        file.write("-----------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Status: {status_msg}\n")
        file.write("===================================\n")

    print(f"\nSession saved successfully as '{filename}' ✅")

else:
    print("\nSession not saved. Exiting program.\n")

print("Thank you for using the Daily Calorie Tracker!")


