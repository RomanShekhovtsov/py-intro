# 3_6 percents
p = int(input())
x = int(input())
y = int(input())
s = float(x * 100  + y) # ����� ������ � ��������
s2 =  s * (100 + p) / 100
print(int(s2 // 100), int(s2 % 100))
