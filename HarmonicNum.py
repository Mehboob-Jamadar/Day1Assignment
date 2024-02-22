n = int(input("Enter the value of N: "))

harmonic = 0
for i in range(1, n + 1):
    # harmonic += 1 / i
    harmonic = harmonic + 1/i

print(f"The {n}th harmonic number is: {harmonic}")
