# 8_03 min_odd
print(
    min (
        filter( lambda x: x % 2 != 0,
            map( int,
                open('input.txt', 'r', encoding='utf8').read().split()
               )
        )
    )
)
