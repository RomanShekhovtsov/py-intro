# 8_01 numbers_count
tests = [1, 2, 3]

print(
    len (
        set(
            open('input.txt', 'r', encoding='utf8').read().split()
        )
    )
)
