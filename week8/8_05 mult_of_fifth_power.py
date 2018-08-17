# 8_05 mult_of_fifth_power
from functools import reduce
print(
    reduce( lambda x, y: x * y,
        map( lambda x: x ** 5,
            map( int,
                open('input.txt', 'r', encoding='utf8').read().split()
               )
        )
    ) 
)
