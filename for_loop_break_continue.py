# Python script for for loop with break and continue

numbers = list(range(1, 11))  # List of numbers from 1 to 10

for num in numbers:
    if num == 3:
        continue  # Skip number 3
    if num == 7:
        break  # Exit loop at 7
    print(num)  # Print numbers

