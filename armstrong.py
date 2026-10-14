
n = int(input("Enter a number: "))
original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** digits
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
