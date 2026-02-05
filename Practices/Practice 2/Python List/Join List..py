#1 example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]

#2 example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3]

#3 example
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
combined = [*list1, *list2, *list3]
print(combined) # [1, 2, 3, 4, 5, 6]

