from typing import List

def find_max(numbers: List[int]) -> int:
    if not numbers:
        print("Not numbers.")
        return 0  # type: ignore
    return max(numbers)

values = [1, 2, 3, 4]  
max_value = find_max(values)
print(max_value)
