# 2_9 cows
n = int(input())
if n > 4 and n < 21:
    r = 'korov'
elif n % 10 == 1:
    r = 'korova'
elif n % 10 < 5 and n % 10 > 0:
    r = 'korovy'
else:
    r = 'korov'
print(n, r)
