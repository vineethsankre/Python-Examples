n = int(input("Enter number: "))
print("before reverse your number is : %d" %n)
reverse = 0
while n != 0:
    reverse = reverse*10 + n%10
    n = (n//10)
print("After reverse : %d" %reverse)