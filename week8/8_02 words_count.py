# 8_02 words_count
tests = [1]

print(
    len (
        set(
            open('input.txt', 'r', encoding='utf8').read().split()
        )
    )
)
