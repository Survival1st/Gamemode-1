#1 example
cities = ["Almaty", "Astana"]
cities.append("Shymkent")
print(cities) # ['Almaty', 'Astana', 'Shymkent']

#2 example
letters = ["A", "C"]
letters.insert(1, "B") # Insert "B" at index 1
print(letters) # ['A', 'B', 'C']

#3 example
numbers = [1, 2]
more_numbers = [3, 4]
numbers.extend(more_numbers)
print(numbers) # [1, 2, 3, 4]

#4 example
list1 = [10, 20]
list2 = [30, 40]
combined = list1 + list2 
print(combined) # [10, 20, 30, 40]

#5 example
colors = ["red", "green"]
colors[len(colors):] = ["blue", "yellow"]
print(colors) # ['red', 'green', 'blue', 'yellow']
