from itertools import batched
from math import sumprod
from tempfile import mkdtemp

init_array = [x+1 for x in range(8)]
result_array = list(batched(init_array, 4))
print(result_array)


prod = sumprod(result_array[0], result_array[1])
print(prod)

print(mkdtemp(dir='.'))
