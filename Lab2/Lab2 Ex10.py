# **Assignment 10: Looping Through a Dictionary**
# **Topic**: Loops Dictionary
# **Objective**: Iterate over keys and values in a dictionary using a for loop.
# 1. Create a dictionary named `inventory` with keys as item names and values as their quantities.
# 2. Use a for loop to iterate over the dictionary and print each key and value pair.
inventory = {
    "apples": 42,
    "bananas": 0,
    "cherries": 520,
}
for i, j in inventory.items():
    print(f"{i}: {j}")



