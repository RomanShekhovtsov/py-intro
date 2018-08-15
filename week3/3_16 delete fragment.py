# 3_16 delete fragment
s = input()
first = s.find('h')
last = s[::-1].find('h')
r = s[:first] + s[len(s)-last:]
print(r)
