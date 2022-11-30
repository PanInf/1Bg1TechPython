a = int(input())
b = int(input())

while b > 0:
    a, b = b, a%b

    temp = a
    a = b
    b = temp%b
print(a)
