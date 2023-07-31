from typing import List

# get the max number in a int list
def find_max(numbers: List[int]) -> int:
    if not numbers:
        return None  # type: ignore[return-value]
    return max(numbers)

values2 = [95, 96, 97, 98, 99, 100]  
max_value2 = find_max(values2)
print(max_value2)
