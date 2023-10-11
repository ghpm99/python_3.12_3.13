def max(list: list[int]) -> None:
    max: int = 0
    for item in list:
        if max < item:
            max = item

    print('max', max)


def print_item(list) -> None:
    print(list)


def sort_item(list: (list[int] | list[str])) -> None:
    sorted_list = sorted(list)
    print(sorted_list)


array_number_obj: list[int] = [1, 2, 3, 52, 44, 7]
array_str_obj: list[str] = ['p', 'y', 't', 'h', 'o', 'n']
array_generic_obj = ['T', 4, 'u', 1, True]


max(array_number_obj)
max(array_str_obj)
max(array_generic_obj)

print_item(array_number_obj)
print_item(array_str_obj)
print_item(array_generic_obj)

sort_item(array_number_obj)
sort_item(array_str_obj)
sort_item(array_generic_obj)
