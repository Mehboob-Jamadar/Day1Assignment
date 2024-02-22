import random
# n = 3
n = int(input("Enter the number of times to flip the coin: "))
heads = 0
tails = 0
for _ in range(n):
    if random.random() < 0.5:
            tails += 1
    else:
            heads += 1

percentage_of_head = (heads / n) * 100
percentage_of_tails = 100 - percentage_of_head

print(f"Percentage of heads: {percentage_of_head: }%")
print(f"Percentage of tails: {percentage_of_tails: }%")