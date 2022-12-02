from typing import List
from pathlib import Path


file_path = Path(__file__).parent.joinpath('input.txt').resolve()
with open(file_path, mode='r') as input_file:
    
    calorie_list: List[int] = []
    total_calories_per_elve: List[int] = []
    for line in input_file:
        print(line.strip())
        if line in ['\n', '\r\n']:
            total_calories_per_elve.append(sum(calorie_list))
            calorie_list.clear()
        else:
            food_item_calorie = int(line.strip())
            calorie_list.append(food_item_calorie)
    
    if len(calorie_list) > 0:
        total_calories_per_elve.append(sum(calorie_list))

print(max(total_calories_per_elve))                 # main
print(sum(sorted(total_calories_per_elve)[-3:]))    # bonus
