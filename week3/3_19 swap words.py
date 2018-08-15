# 3_19 swap words
s = input()
space = s.find(' ')
first = s[:space]
second = s[space + 1:]
reverse = second + ' ' + first
print(reverse)
