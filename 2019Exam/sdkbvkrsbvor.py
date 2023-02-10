x = 2
y = 2
z = 5


def mystical(x, y, z):
    x = x + a
    y = magical(x, y, z)
    z = x * y
    return x + y + z


def magical(a, b, c):
    x = b + a
    y = 1
    z = b + c
    return x / z - y


a = 5
b = 2
c = a // b

ans = int(mystical(a, b, c))
print(ans)
