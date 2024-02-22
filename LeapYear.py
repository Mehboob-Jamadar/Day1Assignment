year = int(input("Enter a year: "))

if len(str(year)) == 4:

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print("Enter a 4 digit number")