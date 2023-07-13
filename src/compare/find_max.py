from typing import List

# get the max number in a int list
def find_max(numbers: List[int]) -> int:
    if not numbers:
        print("Not numbers.")
        return 0  # type: ignore
    return max(numbers)

values = [1, 2, 3, 4]  
max_value = find_max(values)
print(max_value)

values2 = [95, 96, 97, 98, 99, 100]  
max_value2 = find_max(values2)
print(max_value2)
