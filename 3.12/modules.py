from itertools import batched
from math import sumprod

init_array = [x+1 for x in range(8)]
result_array = list(batched(init_array, 4))
print(result_array)


prod = sumprod(result_array[0], result_array[1])
print(prod)
