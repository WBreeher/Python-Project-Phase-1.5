# Just some quick practices and refreshers on loops


# === Example + Definition ===
for x in range(5):  # Will loop  5 times, x = int
    print(x)        # Loops over 0-4 but stops before 5

count = 0           # Beginning variable = 0
while count < 5:    # While count is less than 5
    print(count)    # Program will print current state
    count += 1      # After every printed count, add 1 to total count


# === Loop Objective Drills ===

for i in range(13, 37, 2):
    if i % 10 == 5:
        continue
        print(i)

for i in range(14, 38, 2):
    if i % 10 == 2:
        continue
        print(i)

number = 100
while True:
    a = int(input("enter a number: "))

    if a <= number:
        print("Try again.")
    elif a > number:
        print("Done")
        break

