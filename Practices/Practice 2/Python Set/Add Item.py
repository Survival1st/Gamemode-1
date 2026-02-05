#1 example
birds = {"eagle", "owl"}
birds.add("hawk")

print(birds) # {'eagle', 'owl', 'hawk'} (Order may vary)

#2 example
this_set = {"apple", "banana"}
tropical = {"mango", "pineapple", "papaya"}

this_set.update(tropical)

print(this_set) 
# Output: {'apple', 'mango', 'banana', 'papaya', 'pineapple'}

