number = int(input("Enter a natural number : "))
if number < 1:
    print("Number needs to be greater than 1")
elif number == 1:
    print(number, " is neigher prime nor composite")
else:
    for divisor in range(2, (number//2)+1):
       print(divisor)
