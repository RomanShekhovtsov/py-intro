# 8_04 zero_or_not
print(
    len( list(
        filter( lambda x: x == 0,
            map( int,
                open('input.txt', 'r', encoding='utf8').read().split()[1:]
               )
        )
    ) ) > 0
)
