# 2_4 bissextile year
year = int(input())
if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
    r = 'YES'
else:
    r = 'NO'
print(r)
