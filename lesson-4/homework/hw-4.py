
sample_dict = {0: 10, 1: 20, 2: 30, 3: 15}

asc_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

desc_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)


sample_dict[4] = 40
print("After adding key:", sample_dict)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated = {**dic1, **dic2, **dic3}
print("Concatenated:", concatenated)


n = 5
squares = {x: x*x for x in range(1, n+1)}
print("Squares up to n:", squares)


squares_15 = {x: x*x for x in range(1, 16)}
print("Squares 1 to 15:", squares_15)


my_set = set([1, 2, 3])
print("Created set:", my_set)


for item in my_set:
    print("Set item:", item)


my_set.add(4)
my_set.update([5, 6])
print("After adding members:", my_set)


my_set.discard(2)
print("After discarding 2:", my_set)
my_set.remove(3)
print("After removing 3:", my_set)


item_to_remove = 10
my_set.discard(item_to_remove)
print(f"After discarding {item_to_remove} if present:", my_set)
