from typing import Sequence

type array_number = Sequence[int]
type array_string = Sequence[str]
type generic_array[T: (int, str)] = Sequence[T]


def max(list: array_number) -> None:
    max: int = 0
    for item in list:
        if max < item:
            max = item

    print('max', max)


def print_item(list) -> None:
    print(list)


def sort_item(list: (array_number | array_string)) -> None:
    sorted_list = sorted(list)
    print(sorted_list)


def sum[T](x: T, y: T) -> T:
    return x + y


array_number_obj: array_number = [1, 2, 3, 52, 44, 7]
array_str_obj: array_string = ['p', 'y', 't', 'h', 'o', 'n']
array_generic_obj: generic_array = ['T', 4, 'u', 1, 1.45, True]
array_generic_right: generic_array = ['T', 'u', 4, 65, 'w']


max(array_number_obj)
# max(array_str_obj)
# max(array_generic_obj)

print_item(array_number_obj)
print_item(array_str_obj)
print_item(array_generic_obj)

sort_item(array_number_obj)
sort_item(array_str_obj)
# sort_item(array_generic_obj)

print(sum(1, 2))
# print(sum(1, '2'))


class GenericSum[T]:

    x: T
    y: T

    def __init__(self, x: T, y: T):
        self.x = x
        self.y = y

    def sum(self) -> T:
        return self.x + self.y


sum_int = GenericSum[int](4, 5)
print(sum_int.sum())

sum_str = GenericSum[str]('a', 'b')
print(sum_str.sum())
