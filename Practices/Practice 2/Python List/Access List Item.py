#1 example
langs = ["Python", "Java", "C++", "Ruby"]

print(langs[0])   # "Python"
print(langs[-1])  # "Ruby" (last element)
print(langs[-2])  # "C++" (second to last element)

#2 example
nums = [0, 10, 20, 30, 40, 50, 60]

print(nums[1:4])   # [10, 20, 30]
print(nums[:3])    # [0, 10, 20] (from start to 3rd element)
print(nums[4:])    # [40, 50, 60] (from 4th element to end)
print(nums[::2])   # [0, 20, 40, 60] (every second element)

#3 example
cars = ["Tesla", "BMW", "Audi"]

if "BMW" in cars:
    print("BMW is available!")

#4 example
colors = ["red", "green", "blue"]
pos = colors.index("green") 

print(pos) # 1

#5 example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1])     # [4, 5, 6] (second row)
print(matrix[1][2])  # 6 (second row, third element)