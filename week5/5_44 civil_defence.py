# 5_44 civil_defence
n = int(input())
nn = list(map(int, input().split()))
m = int(input())
mm = list(map(int, input().split()))

towns = []
nearests = []
for i in range(n):
    towns.append((nn[i], i))
    nearests.append(0)

vaults = []
for i in range(m):
    vaults.append((mm[i], i))

towns.sort()
vaults.sort()

vault_nearest = 0
for town in towns:
    vault_i = vault_nearest
    while vault_i < len(vaults) - 1:
        dist_prev = abs(town[0] - vaults[vault_i][0])
        dist_next = abs(town[0] - vaults[vault_i + 1][0])
        if dist_prev < dist_next:
            vault_nearest = vault_i
            break
        vault_i = vault_i + 1
        if vault_i == len(vaults) - 1:
            vault_nearest = vault_i
    nearests[town[1]] = vaults[vault_nearest][1] + 1

print(' '.join(map(str, nearests)))
