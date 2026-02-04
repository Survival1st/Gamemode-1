#1 example
nums = [3, 1, 4, 1, 5]
new_nums = sorted(nums) 
print(new_nums) # [1, 1, 3, 4, 5]
print(nums)     # [3, 1, 4, 1, 5]

nums.sort()
print(nums)     # [1, 1, 3, 4, 5]

#2 example
letters = ["a", "c", "b", "d"]
letters.sort(reverse=True)
print(letters) # ['d', 'c', 'b', 'a']

#3 example
words = ["banana", "pie", "apple", "kiwi"]
words.sort(key=len)
print(words) # ['pie', 'kiwi', 'apple', 'banana']

