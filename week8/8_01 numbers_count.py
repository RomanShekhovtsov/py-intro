# 8_01 numbers_count
tests = [1, 2, 3]

# for t in tests:
#    print(
#        len (
#            set(
#                open('tests/8_01_' + str(t) + '.txt', 'r', encoding='utf8').readlines().split()
#            )
#        )
#    )

print(
    len (
        set(
            open('input.txt', 'r', encoding='utf8').read().split()
        )
    )
)
