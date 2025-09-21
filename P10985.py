n = int(input())
t = 0
def sumofdigit(n):
    sume = 0
    while n > 0:
        sume = sume + n - (n // 10 * 10)
        n = n // 10
    return sume
while n > 0:
    t = t + 1
    n = n - sumofdigit(n)
print(t)
