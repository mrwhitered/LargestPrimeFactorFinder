i = 2
n = int(input("Enter the number: "))
while i < n:
    f = 0
    while not n % i:
        n /= i
        i += 1
        f = 1
    i += 1
    if f:
        i -= 2
print(n)