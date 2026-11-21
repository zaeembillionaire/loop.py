

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

# 3. Print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

# 4. Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 5. Sum from 1 to 100
total = 0
for i in range(1, 101):
    total = total + i

print("Sum =", total)

# 6. Reverse numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

# 7. While loop
i = 1
while i <= 10:
    print(i)
    i += 1