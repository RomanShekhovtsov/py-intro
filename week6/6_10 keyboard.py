# 6_10 keyboard
# data = readtest(6, 10, 1).split('\n')
data = [input(), input(), input(), input()]

keys = int(data[0])
key_capacities = list(map(int, data[1].split()))
pressed_count = int(data[2])
pressed_keys = tuple(map(int, data[3].split()))

for key in pressed_keys:
    key_capacities[key - 1] -= 1

for key in key_capacities:
    if key >= 0:
        print('NO')
    else:
        print('YES')
