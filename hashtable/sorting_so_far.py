# lists keep things in order
my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# why are dictionaries not in order? i.e., order is not guaranteed
## everything hashes differently
## don't know what index the hash function will return

my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]

d = {
    'Austin': 12,
    'Michael': 24,
    'Troy': 35,
    'Jorge': 99,
    'David': 42
}

# how can we sort our dictionary?

# turn into a list
for pair in d.items():
    print(pair)

# d.items().sort()

print(sorted(d.items()))

sorted_list_of_items = list(d.items())
sorted_list_of_items.sort()

print(sorted_list_of_items)