n = int(input("Enter the number: "))

factorial = 1
for i in range(1,n+1):
    factorial = factorial * i

print(f"The Fact num is: {factorial}")