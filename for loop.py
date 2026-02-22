print("=== Dice Rolling Simulation ===")
import random

count_6 = 0
count_1 = 0
count_double_6 = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_double_6 += 1
    
    if roll == 1:
        count_1 += 1
    
    previous_roll = roll

print("\nStatistics:")
print(f"Times rolled a 6: {count_6}")
print(f"Times rolled a 1: {count_1}")
print(f"Times rolled two 6s in a row: {count_double_6}")
print()

print("=== Jumping Jacks Workout ===")
total_jacks = 100
jacks_per_set = 10
completed_jacks = 0

for set_num in range(total_jacks // jacks_per_set):
    print(f"\nDo {jacks_per_set} jumping jacks!")
    completed_jacks += jacks_per_set
    remaining = total_jacks - completed_jacks
    
    if remaining > 0:
        tired = input("Are you tired? (yes/no): ").lower()
        
        if tired in ['yes', 'y']:
            skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
            if skip in ['yes', 'y']:
                break
            else:
                print(f"Great! {remaining} jumping jacks remaining.")
        else:
            print(f"Great! {remaining} jumping jacks remaining.")
    else:
        break

if completed_jacks == total_jacks:
    print("\nCongratulations! You completed the workout!")
else:
    print(f"\nYou completed a total of {completed_jacks} jumping jacks.")