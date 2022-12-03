from functools import reduce

with open("input.txt", mode="r") as f:
    rucksack_data = [line for line in f.read().split("\n") if line != ""]

# create partions
sum_priority_groups = 0
rucksack_groups = [rucksack_data[x : x + 3] for x in range(0, len(rucksack_data), 3)]
for group in rucksack_groups:
    compartment_sets = [set(items) for items in group]

    badge_item = reduce(lambda x, y: x & y, compartment_sets).pop()
    assert badge_item.islower() or badge_item.isupper()
    priority = ord(badge_item) - 96 if badge_item.islower() else ord(badge_item) - 38

    sum_priority_groups += priority

print(sum_priority_groups)
