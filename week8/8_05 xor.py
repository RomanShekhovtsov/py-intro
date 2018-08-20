# 8_05 xor
print(
    *map(lambda x: x[0] ^ x[1],
        list(
            zip(
                *map(lambda l: map(int, l),
                    map(lambda s: s.split(),
                        (input(),input())
))))))
