with open("input.txt", mode="r") as f:

    sum_priorities = 0
    for line in f:
        rucksack_items = list(line)
        compartment_a = rucksack_items[: len(rucksack_items) // 2]
        compartment_b = rucksack_items[len(rucksack_items) // 2 :]

        set_a, set_b = set(compartment_a), set(compartment_b)

        appears_in_both = (set_a & set_b).pop()
        assert appears_in_both.islower() or appears_in_both.isupper()
        priority = (
            ord(appears_in_both) - 96
            if appears_in_both.islower()
            else ord(appears_in_both) - 38
        )

        sum_priorities += priority

    print(sum_priorities)
