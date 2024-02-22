# n = 2
n = int(input("Enter a number: "))
if 0<= n <=31:
    for i in range(n + 1):
        powerof2 = 2**i
        
print(f"2 ^ {i} = {powerof2}")