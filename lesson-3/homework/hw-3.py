

fruits = ["apple", "banana", "cherry", "orange", "grape"]
third_fruit = fruits[2]  
print("The third fruit is:", third_fruit)

numbers1 = [10, 20, 30]
numbers2 = [40, 50, 60]
concatenated_numbers = numbers1 + numbers2
print(concatenated_numbers)

def extract_first_middle_last(numbers):
    if not numbers:
        return []
    first = numbers[0]
    last = numbers[-1]
    middle = numbers[len(numbers)//2]
    return [first, middle, last]

extracted_elements = extract_first_middle_last(concatenated_numbers)
print(extracted_elements)

favorite_movies = ["Inception", "Stranger  things", "Alice in Borderland", "Bruce Almighty", "Man of Steel"]
favorite_movies_tuple = tuple(favorite_movies)
print(favorite_movies_tuple)

cities = ["London", "Berlin", "Paris", "Rome"]
is_paris_in_list = "Paris" in cities
print("Is Paris in the list?", is_paris_in_list)


numbers = [1, 2, 3, 4]
duplicated_numbers = numbers * 2
print("Duplicated list:", duplicated_numbers)


nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping first and last:", nums)


tuple_numbers = tuple(range(1, 11))
slice_tuple = tuple_numbers[3:8]
print("Slice from index 3 to 7:", slice_tuple)


colors = ["blue", "red", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print("Number of times 'blue' appears:", blue_count)


animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print("Index of 'lion':", lion_index)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)


sample_list = [1, 2, 3, 4, 5]
sample_tuple = (10, 20, 30)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))


five_numbers_tuple = (11, 22, 33, 44, 55)
converted_list = list(five_numbers_tuple)
print("Converted list:", converted_list)


num_tuple = (8, 3, 15, 6, 2)
print("Maximum:", max(num_tuple))
print("Minimum:", min(num_tuple))


words_tuple = ("apple", "banana", "cherry", "date")
reversed_tuple = words_tuple[::-1]
print("Reversed tuple:", reversed_tuple)
